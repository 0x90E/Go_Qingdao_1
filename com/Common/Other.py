import re
import subprocess
import time
import hashlib
import os

def md5(content):
    m1 = hashlib.md5()
    m1.update(content)
    return m1.hexdigest()


def __gen_cache_path(id):
    file_name = md5(id)
    return 'com/Files/cache/%s' % file_name


def check_cache(id):
    cache_path = __gen_cache_path(id)
    return os.path.exists(cache_path)


def rename_cache(old_id, new_id):
    try:
        old_path = __gen_cache_path(old_id)
        new_path = __gen_cache_path(new_id)
        if check_cache(old_id):
            os.rename(old_path, new_path)
    except:
        print('rename_cache(%s, %s) err~' % (old_path, new_path))
        pass


def read_cache(id):
    cache_path = __gen_cache_path(id)
    try:
        file = open(cache_path, 'r')
        data = file.read()
        file.close()
        return data
    except:
        return None


def write_cache(id, content):
    pache_path = __gen_cache_path(id)
    try:
        file = open(pache_path, 'w+')
        file.write(content)
        file.close()
        return True
    except:
        return False


def trusted_domain(domain):
    r = domain[-7:].lower()
    if r == '.edu.cn' or r == '.gov.cn':
        return True
    return False


# return: finish, timestamp
def get_domain_regday(domain):
    if domain == 'downza.cn':
        pass
    content = read_cache(domain)
    if not content:
        content = whois(domain)
        if not content:
            return False, None
        write_cache(domain, content)

    # type1 '2003-10-10'
    list_pattern = ['(?<=Registration\ Date\:)(( ?)\d{4}\-\d{1,2}\-\d{1,2})',
                    '(?<=Creation Date:)(( ?)\d{4}\-\d{1,2}\-\d{1,2})',
                    '(?<=Registration\ Time\:)(( ?)\d{4}\-\d{1,2}\-\d{1,2})',
                    '(?<=Record created on)(( ?)\d{4}\-\d{1,2}\-\d{1,2})',
                    '(?<=RegDate:)(( *)\d{4}\-\d{1,2}\-\d{1,2})'
                    ]
    str_reg_date = None
    for pattern in list_pattern:
        try:
            str_reg_date = re.search(pattern, content).group()
            str_reg_date = str_reg_date.strip()
            break
        except:
            pass

    if str_reg_date:
        reg_time = time.strptime(str_reg_date, '%Y-%m-%d')
        reg_timestamp = time.mktime((reg_time.tm_year, reg_time.tm_mon, reg_time.tm_mday, 0, 0, 0, 0, 0, 0))
        return True, reg_timestamp

    # type2: '21-apr-2003'
    try:
        pattern = '(?<=Creation Date:)(( ?)\d{1,2}-[a-zA-Z]{3,4}-\d{4})'
        str_reg_date = re.search(pattern, content).group()
        str_reg_date = str_reg_date.strip()
        reg_time = time.strptime(str_reg_date, '%d-%b-%Y')
        reg_timestamp = time.mktime((reg_time.tm_year, reg_time.tm_mon, reg_time.tm_mday, 0, 0, 0, 0, 0, 0))
        return True, reg_timestamp
    except:
        pass

    # type3: '14-04-2001'
    try:
        pattern = '(?<=Domain Name Commencement Date:)(( ?)\d{1,2}-\d{1,2}-\d{4})'
        str_reg_date = re.search(pattern, content).group()
        str_reg_date = str_reg_date.strip()
        reg_time = time.strptime(str_reg_date, '%d-%m-%Y')
        reg_timestamp = time.mktime((reg_time.tm_year, reg_time.tm_mon, reg_time.tm_mday, 0, 0, 0, 0, 0, 0))
        return True, reg_timestamp
    except:
        pass
    return True, None


def whois(domain):
    retcode, out, err = exec_cmd('whois %s' % domain)
    if out and out.find('Queried interval is too short.') == -1 and out.find('Timeout') == -1:
        return out
    return None


# return : (ret_code, normal, error) or (None, None, None)
def exec_cmd(cmdline, cwd=None, stdout=subprocess.PIPE, stderr=subprocess.PIPE):
    try:
        subp = subprocess.Popen(cmdline, shell=True, stdout=stdout, stderr=stderr, cwd=cwd)
    except Exception, e:
        print(str(e))
        return None, None, None
    out, err = subp.communicate()
    normal = None
    error = None
    if out:
        normal = out.decode(errors='ignore')
    if err:
        error = err.decode()
    return subp.returncode, normal, error


def read_file(path):
    try:
        file = open(path, 'r')
        data = file.read()
        file.close()
        return data
    except:
        return None