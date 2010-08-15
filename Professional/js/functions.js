function setHeadImg()
{ 
  rand = Math.floor(11 * Math.random());
  head =document.getElementById("header");
  head.style.backgroundRepeat = "no-repeat";
  head.style.backgroundPosition= "top center";
  head.style.backgroundImage = "url(./images/headers/head"+rand+".jpg)"; 
}
