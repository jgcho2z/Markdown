#! /usr/bin/python3
import os,re
import sys,getopt
from enum import Enum
from subprocess import call
from functools import reduce

head='''<head> 
<style type="text/css">
body {
  font-family: Helvetica, arial, sans-serif;
  font-size: 14px;
  line-height: 1.6;
  padding-top: 10px;
  padding-bottom: 10px;
  background-color: white;
  padding: 30px;
  color: #333;
}

body > *:first-child {
  margin-top: 0 !important;
}

body > *:last-child {
  margin-bottom: 0 !important;
}

a {
  color: #4183C4;
  text-decoration: none;
}

a.absent {
  color: #cc0000;
}

a.anchor {
  display: block;
  padding-left: 30px;
  margin-left: -30px;
  cursor: pointer;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
}

h1, h2, h3, h4, h5, h6 {
  margin: 20px 0 10px;
  padding: 0;
  font-weight: bold;
  -webkit-font-smoothing: antialiased;
  cursor: text;
  position: relative;
}

h2:first-child, h1:first-child, h1:first-child + h2, h3:first-child, h4:first-child, h5:first-child, h6:first-child {
  margin-top: 0;
  padding-top: 0;
}

h1:hover a.anchor, h2:hover a.anchor, h3:hover a.anchor, h4:hover a.anchor, h5:hover a.anchor, h6:hover a.anchor {
  text-decoration: none;
}

h1 tt, h1 code {
  font-size: inherit;
}

h2 tt, h2 code {
  font-size: inherit;
}

h3 tt, h3 code {
  font-size: inherit;
}

h4 tt, h4 code {
  font-size: inherit;
}

h5 tt, h5 code {
  font-size: inherit;
}

h6 tt, h6 code {
  font-size: inherit;
}

h1 {
  font-size: 28px;
  color: black;
}

h2 {
  font-size: 24px;
  border-bottom: 1px solid #cccccc;
  color: black;
}

h3 {
  font-size: 18px;
}

h4 {
  font-size: 16px;
}

h5 {
  font-size: 14px;
}

h6 {
  color: #777777;
  font-size: 14px;
}

p, blockquote, ul, ol, dl, li, table, pre {
  /*margin: 15px 0;*/
  margin: 6px 0;
}

hr {
  background: transparent url("http://tinyurl.com/bq5kskr") repeat-x 0 0;
  /*border: 0 none;*/
  /*border: 1px solid #cccccc;*/
  color: #f8f8f8;
  /*height: 4px;*/
  height: 1px;
  padding: 0;
}

body > h2:first-child {
  margin-top: 0;
  padding-top: 0;
}

body > h1:first-child {
  margin-top: 0;
  padding-top: 0;
}

body > h1:first-child + h2 {
  margin-top: 0;
  padding-top: 0;
}

body > h3:first-child, body > h4:first-child, body > h5:first-child, body > h6:first-child {
  margin-top: 0;
  padding-top: 0;
}

a:first-child h1, a:first-child h2, a:first-child h3, a:first-child h4, a:first-child h5, a:first-child h6 {
  margin-top: 0;
  padding-top: 0;
}

h1 p, h2 p, h3 p, h4 p, h5 p, h6 p {
  margin-top: 0;
}

li p.first {
  display: inline-block;
}

ul, ol {
  padding-left: 30px;
}

ul :first-child, ol :first-child {
  margin-top: 0;
}

ul :last-child, ol :last-child {
  margin-bottom: 0;
}

dl {
  padding: 0;
}

dl dt {
  font-size: 14px;
  font-weight: bold;
  font-style: italic;
  padding: 0;
  margin: 15px 0 5px;
}

dl dt:first-child {
  padding: 0;
}

dl dt > :first-child {
  margin-top: 0;
}

dl dt > :last-child {
  margin-bottom: 0;
}

dl dd {
  margin: 0 0 15px;
  padding: 0 15px;
}

dl dd > :first-child {
  margin-top: 0;
}

dl dd > :last-child {
  margin-bottom: 0;
}

blockquote {
  /*border-left: 4px solid #dddddd;
   */
  border: 4px solid #dddddd;
  background-color: #f8f8f8;
  padding: 5px 15px;
  color: #777777;
}

blockquote > :first-child {
  margin-top: 0;
}

blockquote > :last-child {
  margin-bottom: 0;
}

table {
  padding: 0;
}
table tr {
  border-top: 1px solid #cccccc;
  background-color: white;
  margin: 0;
  padding: 0;
}

table tr:nth-child(2n) {
  background-color: #f8f8f8;
}

table tr th {
  font-weight: bold;
  border: 1px solid #cccccc;
  text-align: left;
  margin: 0;
  padding: 6px 13px;
}

table tr td {
  border: 1px solid #cccccc;
  text-align: left;
  margin: 0;
  padding: 6px 13px;
}

table tr th :first-child, table tr td :first-child {
  margin-top: 0;
}

table tr th :last-child, table tr td :last-child {
  margin-bottom: 0;
}

img {
  max-width: 100%;
}

span.frame {
  display: block;
  overflow: hidden;
}

span.frame > span {
  border: 1px solid #dddddd;
  display: block;
  float: left;
  overflow: hidden;
  margin: 13px 0 0;
  padding: 7px;
  width: auto;
}

span.frame span img {
  display: block;
  float: left;
}

span.frame span span {
  clear: both;
  color: #333333;
  display: block;
  padding: 5px 0 0;
}

span.align-center {
  display: block;
  overflow: hidden;
  clear: both;
}

span.align-center > span {
  display: block;
  overflow: hidden;
  margin: 13px auto 0;
  text-align: center;
}

span.align-center span img {
  margin: 0 auto;
  text-align: center;
}

span.align-right {
  display: block;
  overflow: hidden;
  clear: both;
}

span.align-right > span {
  display: block;
  overflow: hidden;
  margin: 13px 0 0;
  text-align: right;
}

span.align-right span img {
  margin: 0;
  text-align: right;
}

span.float-left {
  display: block;
  margin-right: 13px;
  overflow: hidden;
  float: left;
}

span.float-left span {
  margin: 13px 0 0;
}

span.float-right {
  display: block;
  margin-left: 13px;
  overflow: hidden;
  float: right;
}

span.float-right > span {
  display: block;
  overflow: hidden;
  margin: 13px auto 0;
  text-align: right;
}

code, tt {
  margin: 0 2px;
  padding: 0 5px;
  white-space: nowrap;
  border: 1px solid #eaeaea;
  background-color: #f8f8f8;
  border-radius: 3px;
}

pre code {
  margin: 0;
  padding: 0;
  white-space: pre;
  border: none;
  background: transparent;
}

.highlight pre {
  background-color: #f8f8f8;
  border: 1px solid #cccccc;
  font-size: 14px;
  line-height: 19px;
  overflow: auto;
  padding: 6px 10px;
  border-radius: 3px;
}

pre {
  background-color: #f8f8f8;
  border: 1px solid #cccccc;
  font-size: 14px;
  line-height: 19px;
  overflow: auto;
  padding: 6px 10px;
  border-radius: 3px;
}

pre code, pre tt {
  background-color: transparent;
  border: none;
}
</style>
</head>'''

class TABLE(Enum):
    Init=1
    Format=2
    Table=3

class ORDERLIST(Enum):
    Init=1
    List=2

class BLOCK(Enum):
    Init=1
    Block=2
    CodeBlock=3

table_state=TABLE.Init
orderList_state=ORDERLIST.Init
block_state=BLOCK.Init
is_code=False
is_normal=True

temp_table_first_line=[]
temp_table_first_line_str=""

need_mathjax=False




def test_state(input):
    Code_List=["python\n","c++\n","c\n"]
    global table_state,orderList_state,block_state,is_code,temp_table_first_line,temp_table_first_line_str

    result=input

    pattern = re.compile(r'```(\s)*\n')
    a=pattern.match(input)

    # BEGIN: block and code block
    if  a and block_state==BLOCK.Init:
        result="<blockquote>"
        block_state=BLOCK.Block
        is_normal=False

    elif len(input)>4 and input[0:3]=='```' and (input[3:9]=="python" or input[3:6]=="c++" or input[3:4]=="c") and block_state==BLOCK.Init:
        block_state=BLOCK.Block
        result="<code></br>"
        is_code=True
        is_normal=False

    elif block_state==BLOCK.Block and input=='```\n':
        if is_code:
            result="</code>"
        else:
            result="</blockquote>"
        block_state=BLOCK.Init
        is_code=False
        is_normal=False

    elif block_state==BLOCK.Block:
        pattern=re.compile(r'[\n\r\v\f\ ]')
        result=pattern.sub("&nbsp",result)
        pattern=re.compile(r'\t')
        result=pattern.sub("&nbsp"*4,result)
        result="<span>"+result+"</span></br>"
        is_normal=False
    # END

    #BEGIN : order list 
    if len(input)>2 and input[0].isdigit() and input[1]=='.' and orderList_state==ORDERLIST.Init:
        orderList_state=ORDERLIST.List
        result="<ol><li>"+input[2:]+"</li>"
        is_normal=False
    elif len(input)>2 and (input[0].isdigit() and input[1]=='.') and orderList_state==ORDERLIST.List:
        result="<li>"+input[2:]+"</li>"
        is_normal=False
    elif len(input)>2 and (input[0].isdigit() and input[1].isdigit() and input[2]=='.') and orderList_state==ORDERLIST.List:
        result="<li>"+input[3:]+"</li>"
        is_normal=False
    elif orderList_state==ORDERLIST.List and (len(input)<=2 or input[0].isdigit()==False or input[1]!='.'):
        result="</ol>"+input
        orderList_state=ORDERLIST.Init
    #END

    #BEGIN: table 
    pattern=re.compile(r'^((.+)\|)+((.+))$')
    match=pattern.match(input)
    if match:
        l=input.split('|')
        l[-1]=l[-1][:-1]
        if l[0] == '':
            l.pop(0)
        if l[-1]=='':
            l.pop(-1)
        if table_state==TABLE.Init:
            table_state=TABLE.Format
            temp_table_first_line=l
            temp_table_first_line_str=input
            result=""

        elif table_state==TABLE.Format :
            if reduce(lambda a,b:a and b,[all_same(i,'-') for i in l],True):
                table_state=TABLE.Table
                result="<table><thread><tr>"
                is_normal=False
           
                for i in temp_table_first_line:
                    result+="<th>"+i+"</th>"
                result+="</tr>"
                result+="</thread><tbody>"
                is_normal=False
            else:
                result=temp_table_first_line_str+"</br>"+input
                table_state=TABLE.Init

        elif table_state==TABLE.Table:
            result="<tr>"
            for i in l:
                result+="<td>"+i+"</td>"
            result+="</tr>"

    elif table_state==TABLE.Table:
        table_state=TABLE.Init
        result="</tbody></table>"+result
    elif table_state==TABLE.Format:
        pass

    #END

    
    return result



def all_same(lst,sym):
    return not lst or sym*len(lst) == lst


def handleTitle(s,n):
    temp="<h"+repr(n)+">"+s[n:]+"</h"+repr(n)+">"
    return temp
        
def handleUnorderd(s):
    s="<ul><li>"+s[1:]
    s+="</li></ul>"
    return s

def tokenTemplate(s,match):
    pattern=""
    if match == '*':
        pattern="\*([^\*]*)\*"
    if match == '~~':
        pattern="\~\~([^\~\~]*)\~\~"
    if match == '**':
        pattern ="\*\*([^\*\*]*)\*\*"
    return pattern

def tokenHandle(s):
    l=['b','i','S']
    j=0
    for i in ['**','*','~~']:
        pattern=re.compile(tokenTemplate(s,i))
        match=pattern.finditer(s)
        k=0
        for a in match:
            if a:
                content=a.group(1)
                x,y=a.span()
                c=3
                if i=='*':
                    c=5
                s=s[:x+c*k]+"<"+l[j]+">"+content+"</"+l[j]+">"+s[y+c*k:]
                k+=1
        pattern=re.compile(r'\$([^\$]*)\$')
        a=pattern.search(s)
        if a:
            global need_mathjax
            need_mathjax=True

        j+=1

    return s

def link_image(s):
    pattern=re.compile(r'\\\[(.*)\]\((.*)\)')
    match=pattern.finditer(s)
    for a in match:
        if a:
            text,url=a.group(1,2)
            x,y=a.span()
            s=s[:x]+"<a href="+url+" target=\"_blank\">"+text+"</a>"+s[y:]


    pattern=re.compile(r'!\[(.*)\]\((.*)\)')
    match=pattern.finditer(s)
    for a in match:
        if a:
            text,url=a.group(1,2)
            x,y=a.span()
            s=s[:x]+"<img src="+url+" target=\"_blank\">"+"</a>"+s[y:]

    pattern=re.compile(r'(.)\^\[([^\]]*)\]')
    match=pattern.finditer(s)
    k=0
    for a in match:
        if a:
            sym,index=a.group(1,2)
            x,y=a.span()
            s=s[:x+8*k]+sym+"<sup>"+index+"</sup>"+s[y+8*k:]
        k+=1
    
    pattern=re.compile(r'(.)/\[(.*)\]')
    match=pattern.finditer(s)
    for a in match:
        if a:
            sym,index=a.group(1,2)
            x,y=a.span()
            s=s[:x]+sym+"<sub>"+index+"</sub>"+s[y:]
    
    return s


def parse(input):
    global block_state,is_normal
    is_normal=True
    result=input

    # BEGIN : ordered list
    if result != "" and result[0].isdigit() and result[1]=='.':
        is_normal=False
    if result != "" and result[0].isdigit() :
        if result[1]=='.' :
            is_normal=False
        elif result[1].isdigit() and result[2]=='.' :
            is_normal=False
    # END
    result=test_state(input)
   
    if block_state==BLOCK.Block :
        return result

    # BEGIN: handle title
    title_rank=0
    for i in range(6,0,-1):
        if input[:i] == '#'*i:
            title_rank=i
            break
    if title_rank!=0:
        result=handleTitle(input,title_rank)
        return result
    # END

    #BEGIN: horizen line 
    if len(input)>2 and all_same(input[:-1],'-') and input[-1]=='\n':
        result="<hr>"
        return result
    #END

    # BEGIN: unordered list
    unorderd=['+','*','-']
    if result != "" and result[0] in unorderd :
        result=handleUnorderd(result)
        is_normal=False
    # END

    f=input[0]
    count=0
    sys_q=False
    while f=='>':
        count+=1
        f=input[count]
        sys_q=True
    if sys_q:
        result=" <blockquote style=\"color:#8fbc8f\"> "*count+"<b>"+input[count:]+"</b>"+"</blockquote>"*count
        is_normal=False

    # BEGIN: token replace,while title and list don't use it,so put it behind them.
    result=tokenHandle(result)
    # END

    #BEGIN: link and image
    result = link_image(result)
    #END
    pa=re.compile(r'^(\s)*$')
    a=pa.match(input)
    if input[-1]=="\n" and is_normal==True and not a :
        result+="</br>"

    return result 


#"""

def print_usage():
    print("Usage: markdown source_file [options]")
    print("source_file suffix must be one of: md, markdown, mdown,mkd")
    print(" Options:")
    print("     -h,--help:    show you help message")
    print("     -o,--output:  set output in specific HTML file,\n \
                if -o is not specified, the default is to put to default_output.html .\n\
                -p,--print    set output in specific PDF  file, this option needs you generate HTML meanwhile.") 
    print("     -P,--Print,   only generate PDF file, you need not to generate HTML file. ")
    


def main():
    dest_file="default_output.html"
    dest_pdf_file=""

    only_pdf=False

    try:
        opts,args = getopt.gnu_getopt(sys.argv[1:],"ho:p:P:",["help","output=","print=","Print="])
        for opt,arg in opts:
            if opt in ["-h","--help"]:
                print_usage()
                sys.exit(1)
            elif opt in ["-o","--output"]:
                dest_file=arg
            elif opt in ["-p","--print"]:
                dest_pdf_file=arg
            elif opt in ["-P","--Print"]:
                dest_pdf_file=arg
                only_pdf=True
            else:
                print("%s====>%s"%(opt,arg))

        if len(args)==1:
            run(args[0],dest_file,dest_pdf_file,only_pdf)
        elif len(args)==0:
            print_usage()
            sys.exit(1)

    except getopt.GetoptError:
        print("Error input!")
        print_usage()
        sys.exit(1)



def run(source_file,dest_file,dest_pdf_file,only_pdf):
    file_name=source_file
    dest_name=dest_file
    dest_pdf_name=dest_pdf_file

    name,suffix=os.path.splitext(file_name)
    if suffix not in [".md",".markdown",".mdown","mkd"]:
        print_usage()
        sys.exit(1)

    if only_pdf:
        dest_name=".~temp~.html"


    f=open(file_name,"r")


    f_r=open(dest_name,"w")
#    f_r.write("<style type=\"text/css\">div {display: block;font-family: \"Times New Roman\",Georgia,Serif}\
#          #wrapper { width: 100%;height:100%; margin: 0; padding: 0;}#left { float:left; \
#         width: 10%;  height: 100%;  }#second {   float:left;   width: 80%;height: 100%;   \
#        }#right {float:left;  width: 10%;  height: 100%; \
#        }</style>")
#    f_r.write("<head> <link rel=\"stylesheet\" href=\"jgcho.css\"> </head>\n")
#    f_r.write("<div id=\"wrapper\"> <div id=\"left\"></div><div id=\"second\">\n")
#    f_r.write("<meta charset=\"utf-8\"/>\n")

    f_r.write(head)

    for eachline in f:
        result=parse(eachline)
        if result!="":
            f_r.write(result)

    f_r.write("</br></br></div><div id=\"right\"></div></div>")

    global need_mathjax
    if need_mathjax:
        f_r.write("<script type=\"text/x-mathjax-config\">\
  MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\\\(','\\\\)']]}});</script><script type=\"text/javascript\" src=\"http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML\"></script>")
    f_r.close()
    f.close()

    if dest_pdf_name != "" or only_pdf:
        call(["wkhtmltopdf",dest_name,dest_pdf_name])
    if only_pdf:
        call(["rm",dest_name])


if __name__=="__main__":
    main() 

