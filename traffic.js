var mapOptions = {
  center: new naver.maps.LatLng(37.5519166830,126.9918205456),
  zoom: 6
};
var map = new naver.maps.Map('map', mapOptions); 

function myfunc1(val){
  GuName_select = val;
  if(val == "AA" ){
    var R = 37.49665824;
    var T = 127.0629816;
  }else if(val == "BB"){
    var R= 37.55045031;
    var T= 127.1470121;
  }else if(val == "CC"){
    var R= 37.643464;
    var T= 127.0111978;
  }else if(val == "DD"){
    var R= 37.56123465;
    var T= 126.8228152;
  }else if(val == "EE"){
    var R= 37.46737968;
    var T= 126.9453427;
  }else if(val == "FF"){
    var R= 37.54671747;
    var T= 127.0857443;
  }else if(val == "GG"){
    var R= 37.49440579;
    var T= 126.8563184;
  }else if(val == "HH"){
    var R= 37.46057121;
    var T= 126.9008254;
  }else if(val == "II"){
    var R= 37.65250722;
    var T= 127.0750488;
  }else if(val == "JJ"){
    var R= 37.66910205;
    var T= 127.0323784;
  }else if(val == "KK"){
    var R= 37.58200946;
    var T= 127.054874;
  }else if(val == "LL"){
    var R= 37.49888197;
    var T= 126.95165;
  }else if(val == "MM"){
    var R= 37.55931747;
    var T= 126.9082652;
  }else if(val == "NN"){
    var R= 37.57778954;
    var T= 126.9390644;
  }else if(val == "OO"){
    var R= 37.47329367;
    var T= 127.0312477;
  }else if(val == "PP"){
    var R= 37.55102736;
    var T= 127.041052;
  }else if(val == "QQ"){
    var R= 37.60570238;
    var T= 127.0175161;
  }else if(val == "RR"){
    var R= 37.5056149;
    var T= 127.1152955;
  }else if(val == "SS"){
    var R= 37.52478534;
    var T= 126.8554572;
  }else if(val == "TT"){
    var R= 37.52231195;
    var T= 126.9101819;
  }else if(val == "UU"){
    var R= 37.53136434;
    var T= 126.9799107;
  }else if(val == "VV"){
    var R= 37.61920928;
    var T= 126.9270219;
  }else if(val == "WW"){
    var R= 37.59491564;
    var T= 126.9773249;
  }else if(val == "XX"){
    var R= 37.56013074;
    var T= 126.9959171;
  }else if(val == "YY"){
    var R= 37.59781724;
    var T= 127.0928845;
  }

  var mapOptions = {
  center: new naver.maps.LatLng(R,T),
  zoom: 8
            
        

  };
  var map = new naver.maps.Map('map', mapOptions); 
}
function myfunc2(val){
   factor_select = val;
   number_factor = 0
   $(".text_num").val(number_factor)
}

function plus(){
  if(factor_select == "trafficlight_num"){
    if(number_factor < 3){
      number_factor = number_factor +1 ;
      console.log(number_factor)
    }
  }
  else if(factor_select == "mean_maxspeed"){
    if(number_factor<30){
    number_factor = number_factor +10}
  }
  $(".text_num").val(number_factor)
}

function minus(){
  if(factor_select == "trafficlight_num"){
    if(number_factor > -3){
    number_factor = number_factor -1}
  }
  else if(factor_select == "mean_maxspeed"){
    if(number_factor > -30){
    number_factor = number_factor -10}
  }
  $(".text_num").val(number_factor)
}  

function create_list(){
  axios.post('http://localhost:5000/test', {
    GuName: GuName_select,
    factor: factor_select,
    value : number_factor
  })
  .then(response=> {
    top5_datas = JSON.parse(response.data)
    top5 = top5_datas.data
    console.log(top5[0]["pred-decline"])
    $('.num1').html("위도:"+top5[0]["Latitude"].toFixed(3)+" 경도:"+top5[0]["Longitude"].toFixed(3));
    $('.num2').html("위도:"+top5[1]["Latitude"].toFixed(3)+" 경도:"+top5[1]["Longitude"].toFixed(3));
    $('.num3').html("위도:"+top5[2]["Latitude"].toFixed(3)+" 경도:"+top5[2]["Longitude"].toFixed(3));
    $('.num4').html("위도:"+top5[3]["Latitude"].toFixed(3)+" 경도:"+top5[3]["Longitude"].toFixed(3));
    $('.num5').html("위도:"+top5[4]["Latitude"].toFixed(3)+" 경도:"+top5[4]["Longitude"].toFixed(3));
    $('.num6').html("위도:"+top5[5]["Latitude"].toFixed(3)+" 경도:"+top5[5]["Longitude"].toFixed(3));
    $('.case1').html(top5[0]["pred-decline"].toFixed(2)+"건")
    $('.case2').html(top5[1]["pred-decline"].toFixed(2)+"건")
    $('.case3').html(top5[2]["pred-decline"].toFixed(2)+"건")
    $('.case4').html(top5[3]["pred-decline"].toFixed(2)+"건")
    $('.case5').html(top5[4]["pred-decline"].toFixed(2)+"건")
    $('.case6').html(top5[5]["pred-decline"].toFixed(2)+"건")
  })
  .catch(error=> {
    console.log(error);
  });
};

function view_map(index){
  var mapOptions = {
  center: new naver.maps.LatLng(top5[index]["Latitude"], top5[index]["Longitude"]),
  zoom: 12
  };
  var map = new naver.maps.Map('map', mapOptions); 
  
  var circle = new naver.maps.Circle({
    map: map,
    center: new naver.maps.LatLng(top5[index]["Latitude"], top5[index]["Longitude"]),
    radius: 20,
    fillColor: 'crimson',
    fillOpacity: 0.6
});
}