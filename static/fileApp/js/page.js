//图片上传预览    IE是用了滤镜。
function previewImage(file)
{
  var MAXWIDTH  = 0;
  var MAXHEIGHT = 0;
  var div = document.getElementById('imghead');
  if(div.style.width){
    var MAXWIDTH  = div.offsetWidth;
    var MAXHEIGHT = div.offsetHeight;
  }

  if (file.files && file.files[0])
  {
      var img = div;
      img.onload = function(){
        var rect = clacImgZoomParam(MAXWIDTH, MAXHEIGHT, img.offsetWidth, img.offsetHeight);
        img.width  =  rect.width;
        img.height =  rect.height;
        img.style.marginTop = rect.top+'px';
      }
      var reader = new FileReader();
      reader.onload = function(evt){img.src = evt.target.result;}
      reader.readAsDataURL(file.files[0]);
  }
  else //兼容IE
  {
    var sFilter='filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(sizingMethod=scale,src="';
    file.select();
    var src = document.selection.createRange().text;
    var img = div;
    img.filters.item('DXImageTransform.Microsoft.AlphaImageLoader').src = src;
    var rect = clacImgZoomParam(MAXWIDTH, MAXHEIGHT, img.offsetWidth, img.offsetHeight);
    status =('rect:'+rect.top+','+rect.left+','+rect.width+','+rect.height);
    div.innerHTML = "<div id=divhead style='width:"+rect.width+"px;height:"+rect.height+"px;margin-top:"+rect.top+"px;"+sFilter+src+"\"'></div>";
  }
}
function clacImgZoomParam( maxWidth, maxHeight, width, height ){
    var param = {top:0, left:0, width:width, height:height};
    if(maxWidth){
      rateWidth = width / maxWidth;
      rateHeight = height / maxHeight;

      if( rateWidth > rateHeight )
      {
          param.width =  maxWidth;
          param.height = Math.round(height / rateWidth);
      }else
      {
          param.width = Math.round(width / rateHeight);
          param.height = maxHeight;
      }
      param.left = Math.round((maxWidth - param.width) / 2);
      param.top = Math.round((maxHeight - param.height) / 2);
    }
    return param;
}

function mouseOver(){
  //var div = document.getElementById('openImgBtn');
  //div.setAttribute("class", "pass-portrait-filebtn-hover");
}

function mouseOut(){
  //var div = document.getElementById('openImgBtn');
  //div.setAttribute("class", "pass-portrait-filebtn");
}

function transFile(){
  var fileDiv = document.getElementById("imghead");
  var formData = new FormData();
  formData.append('img', fileDiv.src);
  var xmlhttp;
  if (window.XMLHttpRequest)
  {
    //  IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
    xmlhttp=new XMLHttpRequest();
  }
  else
  {
    // IE6, IE5 浏览器执行代码
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }

  xmlhttp.onreadystatechange=function()
  {
    if (xmlhttp.readyState==4 && xmlhttp.status==201)
    {
      //json解析
      var json_obj = JSON.parse(xmlhttp.responseText);
      var img_url = json_obj.img

      var trans_url = img_url.replace('file/images/static', 'staticfiles');
      fileDiv.src = trans_url
    }
  }
  xmlhttp.open('post','/file/images/',true);
  xmlhttp.setRequestHeader('Authorization', 'Basic YWlyOjEzOTA4NDA3ODQ5YQ==');
  xmlhttp.send(formData);
}
