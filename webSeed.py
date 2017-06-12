import os
name = raw_input("Select your projectw name: ")
os.system("mkdir " + name)
os.system("touch "+name+"/index.html")
os.system("echo '<!DOCTYPE html>\n" +
"<html lang=\"en\">\n" +
"\t<head>\n" +
"\t\t<meta charset=\"UTF-8\">\n" +
"\t\t<link rel=\"stylesheet\" href=\"css/style.css\">\n" +
"\t\t<meta name=\"viewport\" content=\"width=device-width, user-scalable=no, initial-scale=1.0," +
"maximum-scale=1.0, minimum-scale=1.0\">\n" +
"\t\t<link rel=\"shortcut icon\" type=\"image/x-icon\" href=\"data/imgs/favicon.ico\">\n" +
"\t\t<title>"+name+"</title>\n" +
"\t</head>\n" +
"\t<body>\n" +
"\t\t<div class=\"container\">\n" + 
"\t\t\t<h2>Index of " + name + " project</h2>\n" + 
"\t\t</div>\n" + 
"\t\t <script src=\"js/app.js\"></script>\n" + 
"\t</body>\n" +
"</html>' > "+name+"/index.html")
os.system("mkdir "+name+"/css")
os.system("touch "+name+"/css/style.css")
os.system("echo '*{\n" +
"\tpadding: 0;\n" +
"\tmargin: 0;\n" +
"}\n\n" +
"/* User can not select the tags with this class */\n" +
".no-select{\n" +
"\t-webkit-user-select: none;\n" +
"\t-moz-user-select: none;\n" +
"\t-ms-user-select: none;\n" +
"\tuser-select: none;\n" +
"}\n\n" +
"/* Container */\n" +
".container{\n" +
"\twidth: calc(100vw - 20px);\n" +
"\theight: calc(100vh - 20px);\n" +
"\tpadding: 10px;\n" +
"\toverflow-y: auto\n" + 
"}\n' > "+name+"/css/style.css")
os.system("mkdir "+name+"/js")
os.system("touch "+name+"/js/app.js")
os.system("echo 'var APP = {\n" +
"\tinit: function(){\n" +
"\t\talert(\"Web created succesfuly!\");\n" +
"\t}\n" +
"}\n" +
"APP.init();' > "+name+"/js/app.js")
os.system("mkdir "+name+"/data")
os.system("mkdir "+name+"/data/imgs")
os.system("rm webSeed.py")
os.system("echo Your project was created using webSeed.py")
os.system("open "+name)
os.system("open "+name+"/index.html")