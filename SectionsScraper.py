import re, urllib2

def OPEN_URL(url):
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()
        return link


def web_scrape():
    HTML = OPEN_URL('')
    regex = re.compile('<li><a href="(.+?)">(.+?)</a></li>').findall(HTML)
    for url,name in regex:
        print '<channel>' 
        print '<name>'+(name).replace("%20"," ").replace("&amp;","&").replace("/","")+'</name>'
        print '<thumbnail></thumbnail>'
        print '<externallink></externallink>'
        print '<fanart></fanart>'
        print '<info>'+(name).replace("%20"," ").replace("&amp;","&").replace("/","")+'</info>'
        print '</channel>'
        print
        
def web_scrape2():
    HTML = OPEN_URL('')
    regex = re.compile('<td><a href="(.+?)">(.+?)</td>').findall(HTML)
    for url,name in regex:
        print '<channel>' 
        print '<name>'+(name).replace("%20"," ").replace("&amp;","&").replace("/","")+'</name>'
        print '<thumbnail></thumbnail>'
        print '<externallink></externallink>'
        print '<fanart></fanart>'
        print '<info>'+(name).replace("%20"," ").replace("&amp;","&").replace("/","")+'</info>'
        print '</channel>'
        print

web_scrape()
#web_scrape2()




