# coding=utf8
import urllib
import urllib2


# 全局变量
base_url = "http://tieba.baidu.com/f?"
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
           }


def load_data(html, filename):
    """

    :param html: 要存入的数据
    :param filename: 文件名

    """
    print "正在保存"+filename
    with open(filename, "w") as f:
        f.write(html)


def send_response(full_url, send_headers):
    """

    作用：发送和接受请求
    :param full_url: 拼接后的完整url作为Request的url参数
    :param send_headers: 作为Request的headers参数

    :return: 类文件对象读取后的数据html

    """
    request = urllib2.Request(full_url, headers=send_headers)
    response = urllib2.urlopen(request)
    html = response.read()
    return html


def tb_spider(tb_name, tb_begin, tb_end):
    """

    :param tb_name:贴吧名称
    :param tb_begin:贴吧起始页
    :param tb_end:贴吧终止页

    """
    kw = {"kw": tb_name}
    key_name = urllib.urlencode(kw)
    for page in range(int(tb_begin), int(tb_end)+1):
        page_name = (page-1)*50
        filename = "第" + str(page) + "页.html"
        full_url = base_url+key_name + str(page_name)
        html = send_response(full_url, headers)
        load_data(html, filename)


if __name__ == '__main__':

    name = raw_input("请输入贴吧名称：")
    begin_page = raw_input("请输入开始页面：")
    end_page = raw_input("请输入结束页面：")
    tb_spider(name, begin_page, end_page)
