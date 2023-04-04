
str = ""
str +=('''<!DOCTYPE html>
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
        width: 150px;
        height: auto;
        display: inline-block;
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

import os
l = os.listdir()
tasks = [i for i in l if os.path.isdir(i)]

tasks.sort(key = lambda x:int(x.split('_')[-1]))

for task in tasks:
    images = os.listdir(task)

    str+=(f'''<div class="form-container">
                                <form method="post">
                                    <input type="submit" name="submit_button" value={task}>
                                </form>
                        </div>
                        ''')
    str+=('''<div class="thumbnail-container">
    ''')
    for image in images:
        str+=(f'''<img src="user_upload/{task}/{image}" alt="Thumbnail">
        ''')
    str+=('''</div>
    ''')
str+=('''</div>
                    </div>
                </div>
            </div>
        </div>
    </div>


</body>
</html>''')
with open("base.html","w") as f:
    f.write(str)