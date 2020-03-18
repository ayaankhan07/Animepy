import re
import os
import sys
import time
import urllib
from urllib.request import Request, urlopen
import urllib.request
reqest = Request('https://www.animefreak.tv/home/anime-list', headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(reqest).read().decode("utf-8")
a = re.findall(r'<li><a href="(.*?)"', html)
zyx = input("Whats The Name Of The Anime You Wanna Watch: ")
matching = [s for s in a if zyx in s]
y = -1
while y < len(matching) - 1:
    y += 1
    reqest = Request(matching[y], headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(reqest).read().decode("utf-8")
    a = re.findall(r'">(.*?)</a></li>', html)
    show_images = re.findall(r'src="(.*?)">', html)
    print(str(y) + ": "+ a[8])
ls = int(input("Enter The Number Of Anime You Wanna Watch: "))
print(matching[ls])
req = Request(matching[ls], headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read().decode("utf-8")
lsfile = re.findall(r'<a href="(.*?)">', webpage)
ttle = re.findall('">(.*?)</a></li>',webpage)
print(ttle[8])
x = -1
res = []
while x < len(lsfile) - 1:
    x += 1
    if 'episode' in lsfile[x]:
        if zyx in lsfile[x]:
            b = x- 10
            print(lsfile[x])
            if '/episode/episode-' in lsfile[x]:
                res.append(lsfile[x])
while True:
    print("If You Want To Download It Use The Argument -d")
    q = input("Enter The Number Of Episode You Want To Watch: ")
    if '-d' in q:
        if len(q) == 3:
            l = q[0]
        if len(q) == 4:
            l = q[0]+ '' +q[1]
        if len(q) == 5:
            l = q[0]+ '' +q[1] +''+ q[2]
    else:
        l = q
    a = re.findall(r'h(.*?)/episode/episode-', res[2])
    ep = 'h' + a[0] +'/episode/episode-' + l
    def getep():
        global link, link1
        req = Request(ep, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read().decode("utf-8")
        lsfile = re.findall(r'var file = "(.*?)"', webpage)
        llsfile = len(lsfile[0])
        rlstuff =  lsfile[0][llsfile - 10] +''+ lsfile[0][llsfile - 9]+''+ lsfile[0][llsfile - 8]+''+ lsfile[0][llsfile - 7]+''+ lsfile[0][llsfile - 6]+''+ lsfile[0][llsfile - 5]+''+ lsfile[0][llsfile - 4]+''+ lsfile[0][llsfile - 3]+''+ lsfile[0][llsfile - 2]+''+ lsfile[0][llsfile - 1]
        thing3 = re.findall(r'h(.*?)&', lsfile[0])
        thing2 = 'h'+ thing3[0] + '"&"e='
        thing1 = 'h'+ thing3[0] + '&e='
        link = thing2 + '' + rlstuff
        link1 = thing1 + '' + rlstuff
        if len(link1.split()) > 1:
            if len(link1.split()) == 2:
                link1 = link1.split()[0] +'%20'+ link1.split()[1]
            if len(link1.split()) == 3:
                link1 = link1.split()[0] +'%20'+ link1.split()[1] +'%20'+ link1.split()[2]
            if len(link1.split()) == 4:
                link1 = link1.split()[0] +'%20'+ link1.split()[1] +'%20'+ link1.split()[2] +'%20'+ link1.split()[3]
            if len(link1.split()) == 5:
                link1 = link1.split()[0] +'%20'+ link1.split()[1] +'%20'+ link1.split()[2] +'%20'+ link1.split()[3] +'%20'+ link1.split()[4]
            if len(link1.split()) == 6:
                link1 = link1.split()[0] +'%20'+ link1.split()[1] +'%20'+ link1.split()[2] +'%20'+ link1.split()[3] +'%20'+ link1.split()[4] +'%20'+ link1.split()[5]
            if len(link1.split()) == 7:
                link1 = link1.split()[0] +'%20'+ link1.split()[1] +'%20'+ link1.split()[2] +'%20'+ link1.split()[3] +'%20'+ link1.split()[4] +'%20'+ link1.split()[5] +'%20'+ link1.split()[6]
            if len(link1.split()) == 8:
                link1 = link1.split()[0] +'%20'+ link1.split()[1] +'%20'+ link1.split()[2] +'%20'+ link1.split()[3] +'%20'+ link1.split()[4] +'%20'+ link1.split()[5] +'%20'+ link1.split()[6] +'%20'+ link1.split()[7]
            if len(link1.split()) == 9:
                link1 = link1.split()[0] + '%20' + link1.split()[1] + '%20' + link1.split()[2] + '%20' + link1.split()[3] + '%20' + link1.split()[4] + '%20' + link1.split()[5] + '%20' + link1.split()[6] + '%20' + link1.split()[7] + '%20'+ link1.split()[8]
            if len(link1.split()) == 10:
                link1 = link1.split()[0] +'%20'+ link1.split()[1] +'%20'+ link1.split()[2] +'%20'+ link1.split()[3] +'%20'+ link1.split()[4] +'%20'+ link1.split()[5] +'%20'+ link1.split()[6] +'%20'+ link1.split()[7] +'%20'+ link1.split()[8] +'%20'+ link1.split()[9]
            if len(link1.split()) == 11:
                link1 = link1.split()[0] +'%20'+ link1.split()[1] +'%20'+ link1.split()[2] +'%20'+ link1.split()[3] +'%20'+ link1.split()[4] +'%20'+ link1.split()[5] +'%20'+ link1.split()[6] +'%20'+ link1.split()[7] +'%20'+ link1.split()[8] +'%20'+ link1.split()[9] +'%20'+ link1.split()[10]
            if len(link1.split()) == 12:
                link1 = link1.split()[0] + '%20' + link1.split()[1] + '%20' + link1.split()[2] + '%20' + link1.split()[3] + '%20' + link1.split()[4] + '%20' + link1.split()[5] + '%20' + link1.split()[6] + '%20' + link1.split()[7] + '%20'+ link1.split()[8] +'%20'+ link1.split()[9] +'%20'+ link1.split()[10] +'%20'+ link1.split()[11]
            if len(link1.split()) == 13:
                link1 = link1.split()[0] +'%20'+ link1.split()[1] +'%20'+ link1.split()[2] +'%20'+ link1.split()[3] +'%20'+ link1.split()[4] +'%20'+ link1.split()[5] +'%20'+ link1.split()[6] +'%20'+ link1.split()[7] +'%20'+ link1.split()[8] +'%20'+ link1.split()[9] +'%20'+ link1.split()[10] +'%20'+ link1.split()[11] +'%20'+ link1.split()[12]

        if len(link.split()) > 1:
            if len(link.split()) == 2:
                link = link.split()[0] +'%20'+ link.split()[1]
            if len(link.split()) == 3:
                link = link.split()[0] +'%20'+ link.split()[1] +'%20'+ link.split()[2]
            if len(link.split()) == 4:
                link = link.split()[0] +'%20'+ link.split()[1] +'%20'+ link.split()[2] +'%20'+ link.split()[3]
            if len(link.split()) == 5:
                link = link.split()[0] +'%20'+ link.split()[1] +'%20'+ link.split()[2] +'%20'+ link.split()[3] +'%20'+ link.split()[4]
            if len(link.split()) == 6:
                link = link.split()[0] +'%20'+ link.split()[1] +'%20'+ link.split()[2] +'%20'+ link.split()[3] +'%20'+ link.split()[4] +'%20'+ link.split()[5]
            if len(link.split()) == 7:
                link = link.split()[0] +'%20'+ link.split()[1] +'%20'+ link.split()[2] +'%20'+ link.split()[3] +'%20'+ link.split()[4] +'%20'+ link.split()[5] +'%20'+ link.split()[6]
            if len(link.split()) == 8:
                link = link.split()[0] +'%20'+ link.split()[1] +'%20'+ link.split()[2] +'%20'+ link.split()[3] +'%20'+ link.split()[4] +'%20'+ link.split()[5] +'%20'+ link.split()[6] +'%20'+ link.split()[7]
            if len(link.split()) == 9:
                link = link.split()[0] + '%20' + link.split()[1] + '%20' + link.split()[2] + '%20' + link.split()[3] + '%20' + link.split()[4] + '%20' + link.split()[5] + '%20' + link.split()[6] + '%20' + link.split()[7] + '%20'+ link.split()[8]
            if len(link.split()) == 10:
                link = link.split()[0] +'%20'+ link.split()[1] +'%20'+ link.split()[2] +'%20'+ link.split()[3] +'%20'+ link.split()[4] +'%20'+ link.split()[5] +'%20'+ link.split()[6] +'%20'+ link.split()[7] +'%20'+ link.split()[8] +'%20'+ link.split()[9]
            if len(link.split()) == 11:
                link = link.split()[0] +'%20'+ link.split()[1] +'%20'+ link.split()[2] +'%20'+ link.split()[3] +'%20'+ link.split()[4] +'%20'+ link.split()[5] +'%20'+ link.split()[6] +'%20'+ link.split()[7] +'%20'+ link.split()[8] +'%20'+ link.split()[9] +'%20'+ link.split()[10]
            if len(link.split()) == 12:
                link = link.split()[0] + '%20' + link.split()[1] + '%20' + link.split()[2] + '%20' + link.split()[3] + '%20' + link.split()[4] + '%20' + link.split()[5] + '%20' + link.split()[6] + '%20' + link.split()[7] + '%20'+ link.split()[8] +'%20'+ link.split()[9] +'%20'+ link.split()[10] +'%20'+ link.split()[11]
            if len(link.split()) == 13:
                link = link.split()[0] +'%20'+ link.split()[1] +'%20'+ link.split()[2] +'%20'+ link.split()[3] +'%20'+ link.split()[4] +'%20'+ link.split()[5] +'%20'+ link.split()[6] +'%20'+ link.split()[7] +'%20'+ link.split()[8] +'%20'+ link.split()[9] +'%20'+ link.split()[10] +'%20'+ link.split()[11] +'%20'+ link.split()[12]

            return link
        else:
            return link

    def reporthook(count, block_size, total_size):
        global start_time
        if count == 0:
            start_time = time.time()
            return
        duration = time.time() - start_time
        progress_size = int(count * block_size)
        speed = int(progress_size / (1024 * duration))
        percent = int(count * block_size * 100 / total_size)
        sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
                         (percent, progress_size / (1024 * 1024), speed, duration))
        sys.stdout.flush()


    def save(url, filename):
        urllib.request.urlretrieve(url, filename, reporthook)
    ep1 = getep()
    if '-d' in q:
        opener = urllib.request.URLopener()
        opener.addheader('User-Agent', 'Mozirilla/5.0')
        save = save(link1, 'ep-' + l + '-' + ttle[8] + '.mp4')
    else:
        if '==' in ep1:
            os.system("mplayer " + getep())
        else:
            os.system("mplayer " + ep1)
