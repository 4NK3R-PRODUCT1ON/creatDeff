# -*- coding: utf-8 -*-
import os, sys
h = '\x1b[0;32m'
ht = '\x1b[32;1m'
b = '\x1b[34;1m'
k = '\x1b[93;1m'
e = '\x1b[93;2m'
me = '\x1b[31;1m'
cy = '\x1b[36;1m'
u = '\x1b[35;1m'
pu = '\x1b[37;1m'
hi = '\x1b[30;1m'
hp = '\x1b[92;7m'
x = '\x1b[0m'
print ''
print {$me}'╔═══╦═╗─╔╦╗╔═╦═══╦═══╗╔═══╦═══╦═══╦═══╦═══╦═══╗'
print {$me}'║╔═╗║║╚╗║║║║╔╣╔══╣╔═╗║╚╗╔╗║╔══╣╔══╣╔═╗║╔═╗║╔══╝'
print {$me}'║║─║║╔╗╚╝║╚╝╝║╚══╣╚═╝║─║║║║╚══╣╚══╣║─║║║─╚╣╚══╗'
print {$me}'║╚═╝║║╚╗║║╔╗║║╔══╣╔╗╔╝─║║║║╔══╣╔══╣╚═╝║║─╔╣╔══╝'
print {$me}'║╔═╗║║─║║║║║╚╣╚══╣║║╚╗╔╝╚╝║╚══╣║──║╔═╗║╚═╝║╚══╗'
print {$me}'╚╝─╚╩╝─╚═╩╝╚═╩═══╩╝╚═╝╚═══╩═══╩╝──╚╝─╚╩═══╩═══╝'
print {$me}'[+]AUTOR=ANKER PRODUCTION'
print ''
title = raw_input('[+] Judul/Title >> ')
gambar = raw_input('[+] Logo/Gambar >> ')
hack = raw_input('[+] Hacked by >> ')
team = raw_input('[+] Team >> ')
pesan = raw_input('[+] Pesan (Note : Gunakan <br> untuk baris baru) (gunakan <i> agar tulisan bercetak miring) >> ')
thanks = raw_input('[+] Thanks to >> ')
nomor = raw_input('[+] Nomer Whatsapp >> ')
lagu = raw_input('[+] Link Musik >> ')
fo = open('ANKER.html', 'w')
tod1 = '<html>\n <head>\n<title>'
tod2 = title
tod3 = '</title>\n <link rel="icon" type="image/x-icon" href="">\n <meta name="description" content="Terkentod">\n<meta name="keywords" content="ANKER">\n<meta name="googlebot" content="index,follow" /> <meta name="robots" content="all" />\n <meta name="robots schedule" content="auto" />\n <meta name="distribution" content="global" />\n <meta contact=\'#\' />\n <meta charset="utf-8">\n  <link href="https://fonts.googleapis.com/css?family=Iceland" rel="stylesheet" type="text/css">\n  <style>\n html, body { background-color: #000 ; height: 100vh; margin: 0; } .full-height { \theight: 100vh; } .flex-center { \talign-items: center; display: flex; justify-content: center; } .position-ref { position: relative; } .content { text-align: center; } .title { font-size: 36px; padding: 20px; } </style> </head>\n <body align="center" oncontextmenu="return false">\n <script type="text/javascript"> </script> <div class="flex-center position-ref full-height">\n <div class="content">\n <div class="text">\n<center>\n<img src=\''
tod4 = gambar
tod5 = '\' height="350">\n <br>\n<br>\n<font color="white" size="30px" face="Iceland">Hacked by <font color="red">'
tod6 = hack
tod7 = '</font>|'
tod8 = team
tod9 = '</font>\n<hr color="red" width="30%">\n<marquee behavior="Alternate" direction="right" scrollamount="20"><font color="red" size="6" face="Iceland">Security Get Down!!!</font></marquee>\n<br>\n<hr color="red" width="30%">\n<center>\n<font face="Iceland" size="7" color="white">message: <br>'
tod10 = pesan
tod11 = '<br><font color="red">'
tod12 = team
tod13 = '</font>\n<br>\n<marquee behavior="Alternate" direction="right" scrollamount="80"><font color="red">--------------------</font></marquee>\n<br>\n<font size="8" color="white">Greetz: <br>'
tod14 = thanks
tod15 = '<br>\n<marquee behavior="Alternate" direction="right" scrollamount="80"><font color="red">--------------------</font></marquee>\n</center>\n<br>\n<br>\n<a href="https://wa.me/'
tod16 = nomor
tod17 = '><font color="red">contact</font></a>\n<br>\n<font color="red">NO WEBSITE!!! \n<br>\n       <iframe width="1" height="1" src=\''
tod18 = lagu
tod19 = '\'frameborder="0" allowfullscreen></iframe>\n<br>\n<script src="https://cdn.rawgit.com/bungfrangki/efeksalju/2a7805c7/efek-salju.js" type="text/javascript"> </script> \n <script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script></body>\n</html>'
fo.write(tod1)
fo.write(tod2)
fo.write(tod3)
fo.write(tod4)
fo.write(tod5)
fo.write(tod6)
fo.write(tod7)
fo.write(tod8)
fo.write(tod9)
fo.write(tod10)
fo.write(tod11)
fo.write(tod12)
fo.write(tod13)
fo.write(tod14)
fo.write(tod15)
fo.write(tod16)
fo.write(tod17)
fo.write(tod18)
fo.write(tod19)
print ''
print '[+] Sukses Membuat DEFACE ANKER [+]'
print '[+] Silahkan Tulis cp ANKER.html /sdcard [+]'
print '[+] Terimakasih telah menggunakan DEFACE ANKER [+]'
fo.close()
