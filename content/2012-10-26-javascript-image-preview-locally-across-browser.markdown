Author: levin
Date: 2012-10-26 18:25
disqus_identifier: 201210261825
Slug: javascript-image-preview-locally-across-browser
Title: 兼容多浏览器的本地图片预览js脚本
Category: Web
Tags: javascript

<!-- more -->

HTML代码：

    <input type="file" value="" name="imgfile" id="imgfile">
    <!--[if IE]>
    <div id="ieimgpreview"></div>
    <![endif]-->
    <img src="" id="imgpreview">

JS代码：

    var ie = ! ','.split(/,/).length;			//判断IE系列浏览器
    $(document).ready(function(){
    	$('#imgpreview').hide();
    	$('#imgfile').change(function(){
    		if (ie) {		//处理ie，原理是div的背景渲染
    			var ieimgpreview = document.getElementById('ieimgpreview');
    			ieimgpreview.style.width = "118px";
    			ieimgpreview.style.height = "127px";
    			ieimgpreview.style.filter="progid:DXImageTransform.Microsoft.AlphaImageLoader(sizingMethod = scale)";
    			ieimgpreview.filters.item("DXImageTransform.Microsoft.AlphaImageLoader").src = this.value;
    		} else {
    			try {		//处理火狐，直接替换img标签的src为图片的base64字符
    				$('#imgpreview')[0].src = window.URL.createObjectURL(this.files[0]);
    			}
    			catch (e) {		//处理chrome和支持html5的浏览器，也是直接替换img标签的src为图片的base64字符
    				var reader = new FileReader();
    				if (/image\/\w+/.test(this.files[0].type)) {
    					reader.onload = function() {
    						$('#imgpreview')[0].src = this.result;
    					}
    					reader.readAsDataURL(this.files[0]);
    				}
    			}
    			$('#imgpreview').show();
    		}
    	});
    });

