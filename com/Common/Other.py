import re
import subprocess
import time
import hashlib


def md5(content):
    m1 = hashlib.md5()
    m1.update(content)
    return m1.hexdigest()


def read_cache(id):
    file_name = md5(id)
    try:
        file = open('com/Files/cache/%s' % file_name, 'r')
        data = file.read()
        file.close()
        return data
    except:
        return None


def write_cache(id, content):
    file_name = md5(id)
    try:
        file = open('com/Files/cache/%s' % file_name, 'w+')
        file.write(content)
        file.close()
        return True
    except:
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
    list_pattern = ['(?<=Registration\ Date\: )(\d{4}\-\d{1,2}\-\d{1,2})',
                    '(?<=Creation Date: )(\d{4}\-\d{1,2}\-\d{1,2})',
                    '(?<=Registration\ Time\: )(\d{4}\-\d{1,2}\-\d{1,2})'
                    ]
    str_reg_date = None
    for pattern in list_pattern:
        try:
            str_reg_date = re.search(pattern, content).group()
            break
        except:
            pass

    if str_reg_date:
        reg_time = time.strptime(str_reg_date, '%Y-%m-%d')
        reg_timestamp = time.mktime((reg_time.tm_year, reg_time.tm_mon, reg_time.tm_mday, 0, 0, 0, 0, 0, 0))
        return True, reg_timestamp

    # type2: '21-apr-2003'
    try:
        pattern = '(?<=Creation Date: )(\d{1,2}-[a-zA-Z]{3,4}-\d{4})'
        str_reg_date = re.search(pattern, content).group()
        reg_time = time.strptime(str_reg_date, '%d-%b-%Y')
        reg_timestamp = time.mktime((reg_time.tm_year, reg_time.tm_mon, reg_time.tm_mday, 0, 0, 0, 0, 0, 0))
        return True, reg_timestamp
    except:
        return True, None





def whois(domain):
    retcode, out, err = exec_cmd('whois %s' % domain)
    if out:
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
