Author: levin
Date: 2014-08-06 00:50
disqus_identifier: 201408060050
Slug: uploading-files-with-ajax-based-on-base64-text-encoding
Title: 将文件编码成base64通过AJAX上传
Category: Web
Tags: jQuery

使用AJAX是无法直接上传文件的，一般都是新建个iframe在它里面完成表单提交的过程以达到异步上传文件的效果。<!-- more -->

如此做可以达到比较好的浏览器兼容性，不过代码量会比较大，即使是使用了文件上传插件，例如[plupload](/url.html#http://www.plupload.com/)。

如何能达到灵活的程度呢，能像普通的AJAX提交表单数据那样将文件看成是普通表单参数来对待就好了。

灵光一闪，利用javascript的FileReader对象将文件编码成base64再传服务器不就行了么~

开始动手，丰衣足食。

前端对文件进行base64编码并通过ajax向服务器传输：

    <head>
        <meta charset="UTF-8">
    </head>
    
    <form onsubmit="return false;">
        <input type="hidden" name="file_base64" id="file_base64">
        <input type="file" id="fileup">
        <input type="submit" value="submit" onclick="$.post('./uploader.php', $(this).parent().serialize());">
    </form>
    
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
    <script>
    $(document).ready(function(){
    	$("#fileup").change(function(){
    		var v = $(this).val();
    		var reader = new FileReader();
    		reader.readAsDataURL(this.files[0]);
    		reader.onload = function(e){
    			console.log(e.target.result);
    			$('#file_base64').val(e.target.result);
    		};
    	});
    });
    </script>

后端对文件数据解码并保存：

    <?php
    
    if (isset($_POST['file_base64'])){
    	$file_base64 = $_POST['file_base64'];
    	$file_base64 = preg_replace('/data:.*;base64,/i', '', $file_base64);
    	$file_base64 = base64_decode($file_base64);
    	
    	file_put_contents('./file.save', $file_base64);
    }

javascript里的FileReader对象主流浏览器都支持，IE10以上支持，私认为在为小范围提供服务时可以考虑这个异步上传文件的方式，省时又省力，兼容IE系列另当别论。

Reference:

1. [FileReader - Web API Interfaces | MDN](/url.html#https://developer.mozilla.org/en-US/docs/Web/API/FileReader)
