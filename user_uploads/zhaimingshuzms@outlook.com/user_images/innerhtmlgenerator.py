head =('''<!DOCTYPE html>
<html lang="en">
<head>
<style>
    .form-container {
        width: 100%;
    }
    .form-container form {
        display: inline-block;
    }
    .thumbnail-container {
    width: 100%;
    }
    .thumbnail-container img {
        width: 45%;
        height: auto;
    }
    ul{
        float: left;
        list-style-type: none;
        margin: 15px;
    }
    ul li{
        display: inline-block;
    }

    ul li a{
        text-decoration: none;
        color: #c22e2e;
        padding: 5px 20px;
        border: 1px solid transparent;
        transition: .6s ease;
        border-radius: 20px;
    }

    ul li a:hover{
        background-color: #864747;
        color: #000;
    }
    ul li.active a{
        background-color: #fb0404;
        color: #000;
    }
    .title{
        position: absolute;
        top:50%;
        left:50%;
        transform: translate(-50%,-50%);
    }
    .title h1{
        color: #fff;
        font-size: 70px;
        font-family: Century Gothic;
    }
</style>
<meta http-equiv="content-type" content="text/html; charset=utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1, viewport-fit=cover"/>
<title>Record Picture</title>
<!--========================================CSS=======================================================-->
<link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/@fontsource/saira-extra-condensed@4.5.0/index.min.css"/>
<link rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@5.15.4/css/all.min.css"/>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/devicons/devicon@v2.13.0/devicon.min.css"/>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css"/>
<link rel="stylesheet" href="../static/css/main.css"/>

</head>
<body>


<!--====================================1.设置侧边框===========================================================-->
<aside id="sidebar" class="menu is-hidden-touch">
</aside>
<div id="content">
    <div id="fullpage">
        <!--===========================展示所有照片=============================================-->
        <div class="section hero is-fullheight page" id="anchor_1" style="padding: 1rem 3rem;">    <!--修改padding-->
            <!--图片区域顶部-->
                <!--第一张浮窗图片-->
            <div class="col-lg-3 col-md-6">
                <div class="featured-item pd-bottom-90">
                    <div class="featured-item-meta">
                    ''')

tail=('''</div>
                    </div>
                </div>
            </div>
        </div>
    </div>


</body>
</html>''')

import os
l = os.listdir()
tasks = [i for i in l if os.path.isdir(i)]

tasks.sort(key = lambda x:int(x.split('_')[-1]))

for task in tasks:
    images = os.listdir(task)
    str = ""
    str+=(f'''<ul>
                                <li><a href="../../base.html" target="_blank">Back</a></li>
                            </ul>
                            <br />
                        ''')
    str+=('''<div class="thumbnail-container">
    ''')
    for image in images:
        if os.path.splitext(image)[-1]!='.png':
            continue
        str+=(f'''<img src={image} alt="Thumbnail">
        ''')
    str+=('''</div>
    ''')

    with open(f"{task}/base.html","w") as f:
        f.write(head+str+tail)