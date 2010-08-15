#! /usr/bin/env python2.4

from subprocess import *


html_header = R"""

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<!--this design was created by Vacant (Chris Blunden), http://www.web-site.tk .
Deep, version 1.5 created on 17/10/04 for OSWD.org ... DO NOT REMOVE this notice. Thanks. -->

<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />



      <title>Andy R Terrel</title>
      <link rel="stylesheet" type="text/css" href="styles/entrance_style.css" />
      <script type="text/javascript" src="js/functions.js"></script>

  </head>

  <body onload="setQuote();">
    <div id="outer">
      <div id="inner">

        <div class="bgtext">Andy R Terrel</div>
        <div id="footertext">Every man's life, truly told, is a novel. </div>


         <div id="close"><a href="index.html" title="close and return to menu">X</a></div>
         <div id="top"><a href="#top" title="back to top">^</a></div>

  	  <!--greyed out links-->
	  <div id="text1">about this site</div>
	  <div id="text2">I Compute Stuff</div>
	  <div id="text3">I hate Mondays</div>
	  <div id="text4">Something's Burning</div>
	  <div id="text5">Still searching for truth</div>
	  <div id="text7">contact me</div>
          <div id="text8">Hot off the press!</div>
	  <div id="text9">Hooked of foniks</div>
          <!--greyed out links end-->

	  <div id="urltext"><a href="index.html" class="navigurl"
	  title="click to return to the index page">index &raquo;
	  </a>new_stuff</div>

	  <div id="content"> <a name="top"></a> <!-- very important!
	  this is the anchor for the back to top feature. Remove it at
	  your own risk! :P -->

	    <div class="titleblock">New stuff on my website</div>
	    So here is an automatically generated list of files that have been
            updated recently minus things that are dynamic or offsite (i.e. my blog).
            Just so you know what is current and what is not.<p />



            <ul>
"""

html_footer = R"""
            </ul><p />&nbsp
	   </div>
	 </div>
       </div>

<script src="http://www.google-analytics.com/urchin.js" type="text/javascript">
</script>
<script type="text/javascript">
_uacct = "UA-388278-1";
urchinTracker();
</script>
  </body>

</html>
"""

def getFilelist():
    cmd = "ls -R ."
    p = Popen(cmd, shell=True, stdout=PIPE, close_fds=True)
    lines = p.stdout.readlines()
    dir = ""
    list_of_files = []
    for l in lines:
        if l.find(':\n') >= 0:
            dir = l[:l.find(':')]+'/'
            dir = dir.replace('.', '')
        if l.find('.html') >= 0:
            x = l.split()
            if x[-1].find("target") >= 0:
                x[-1] = "index.html"
            if x[-1] == "new_stuff.html":
                continue
            list_of_files.append( dir[1:]+x[-1] )
    unique_list = []
    for x in list_of_files:
        if not x in unique_list:
            unique_list.append(x)
    list_of_files = unique_list
    list_of_files.sort(reverse = True)
    return list_of_files

def generateHTMLFile(text):
    fp=open("new_stuff.html",'w')
    fp.write(html_header)
    fp.write(text)
    fp.write(html_footer)
    fp.close()

def generateNewItems(n):
    list_of_files = getFilelist()[:n]
    return "\n".join(map(lambda(x):'<li><a href="'+x[1]+'">'+x[1]+'</a> -- '+x[0]+'</li>', list_of_files))


def changeFooters(footerText):
    filelist = getFilelist()
    print filelist
    for f in  filelist:
        fp = open(f)
        file = fp.read()
        fp.close()
        if file.find('<div id="footer">')> -1:
            print "Changing "+f
            start = file.find('<div id="footer">')+17
            stop = file.find('</div>', start)
            new_file = file[:start]+footerText+file[stop:]
            fp2=open(f,'w')
            fp2.write(new_file)
            fp2.close()

def changePersonalMenus(menuText):
    filelist = getFilelist()
    filelist = filter(lambda i: "Personal/index" in i[1],filelist)
    for f in [i[1] for i in filelist]:
        fp = open(f)
        file = fp.read()
        fp.close()
        if file.find('<div id="header">')> -1:
            if file.find('<div id="menu">')> -1:
                print "Changing "+f
                start = file.find('<div id="menu">')+16
                stop = file.find('</div>', start)
                new_file = file[:start]+menuText+file[stop:]
                fp2=open(f,'w')
                fp2.write(new_file)
                fp2.close()




if __name__=="__main__":
    footer =R"""
    <a href="/">Main</a> |
    <a href="/Professional/">Professional</a> |
    <a href="/Teaching/">Teaching</a>
    <br/>&copy;2006-2009 Andy R. Terrel
    """
    changeFooters(footer)

    menu = R"""
    <ul>
    <li><a href="/Personal/index.html" title="Main Personal Page">Personal</a></li>
    <li><a href="/Personal/Photos/index.html" title="view photos">Photos</a></li>
    <li><a href="/Personal/Cooking/index.html" title="I love to cook" class="active">Cooking</a></li>
    </ul>
    """
    #changePersonalMenus(menu)

    #text = generateNewItems(15)
    #generateHTMLFile(text)
