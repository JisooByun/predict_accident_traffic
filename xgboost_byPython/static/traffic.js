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

  mapOptions = {
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
  if(factor_select == "trafficlight_num"||factor_select == "crosswalk_num"||factor_select == "mean_lanes"){
    if(number_factor < 2){
      number_factor = number_factor +1 ;
      console.log(number_factor)
    }
  }
  else if(factor_select == "mean_wth"){
    if(number_factor<10){
    number_factor = number_factor +5}
  }else if(factor_select=="mediansep_"||factor_select=="island_num"||factor_select=="school_num"){
    if(number_factor<1){
      number_factor = number_factor +1
    }
  }
  $(".text_num").val(number_factor)
}

function minus(){
  if(factor_select == "trafficlight_num"||factor_select == "crosswalk_num"||factor_select == "mean_lanes"){
    if(number_factor > -2){
      number_factor = number_factor -1 ;
      console.log(number_factor)
    }
  }
  else if(factor_select == "mean_wth"){
    if(number_factor>-10){
    number_factor = number_factor -5}
  }else if(factor_select=="mediansep_"||factor_select=="island_num"||factor_select=="school_num"){
    if(number_factor>-1){
      number_factor = number_factor -1
    }
  }
  $(".text_num").val(number_factor)
}  

function create_list(){
  if(typeof GuName_select === "undefined"){
  isloading.stop();
  alert("구를 선택해주세요.");
  }
  else if(typeof factor_select === "undefined"){
  isloading.stop();
  alert("요인을 선택해주세요.");
  }
  else if(number_factor == 0){
  isloading.stop();
  alert("값을 선택해주세요.")
  }
  else{
  axios.post('http://localhost:5000/test', {
    GuName: GuName_select,
    factor: factor_select,
    value : number_factor
  })
  .then(response=> {
    top5_datas = JSON.parse(response.data)
    top5 = top5_datas.data
    console.log(top5)
    isloading.stop()
    for(i = 0; i<6; i++){
    $('.num'+(i+1)).html("위도:"+top5[i]["Latitude"].toFixed(3)+" 경도:"+top5[i]["Longitude"].toFixed(3));
    $('.acc_num'+(i+1)).html(top5[i]["total_acc"].toFixed(0)+"건")
    $('.case'+(i+1)).html(top5[i]["pred-decline"].toFixed(2)+"건")
    $('.prob'+(i+1)).html((top5[i]["pred-decline"]/top5[i]["total_acc"]*100).toFixed(2)+"%")
    }
    myfunc1(top5[0]["gu_code"])
    var map = new naver.maps.Map('map', mapOptions); 
    for(index =0 ; index<top5.length ;index++){
      var circle = new naver.maps.Circle({
      map: map,
      center: new naver.maps.LatLng(top5[index]["Latitude"], top5[index]["Longitude"]),
      radius: 100+300*(top5[index]["total_acc"]/300),
      fillColor: 'crimson',
      fillOpacity: 0.2+1.5*(top5[index]["total_acc"]/300)
     })
  };
})
  .catch(error=> {
    console.log(error);
  });}
};



function view_map(index){
  $(".info0").html(index+1)
  $(".info1").html(top5[index]["Latitude"].toFixed(3))
  $(".info2").html(top5[index]["Longitude"].toFixed(3))
  $(".info3").html(top5[index]["trafficlight_num"])
  $(".info4").html(top5[index]["crosswalk_num"])
  $(".info5").html(top5[index]["mean_lanes"].toFixed(1))
  $(".info6").html(top5[index]["mean_speed"])
  $(".info7").html(top5[index]["island_num"])
  $(".info8").html(top5[index]["mediansep_"])
  $(".info9").html(top5[index]["school_num"])
  $(".info10").html(top5[index]["police_num"])
  $(".info11").html(top5[index]["station_num"])

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
// function create_list2(){
//     axios.post('http://localhost:5000/graph', {
//     GuName: GuName_select,
//     factor: factor_select
//     })
//     .then(response=> {
//     graph_datas = JSON.parse(response.data)
//     graph5 = graph_datas.data
//     console.log(graph5)
//     })
//     .catch(error=> {
//         console.log(error);
//       });
// }

isloading = {
  start: function() {
    if (document.getElementById('wfLoading')) {
      return;
    }
    var ele = document.createElement('div');
    ele.setAttribute('id', 'wfLoading');
    ele.classList.add('loading-layer');
    ele.innerHTML = '<span class="loading-wrap"><span class="loading-text"><span>.</span><span>.</span><span>.</span></span></span>';
    document.body.append(ele);

    // Animation
    ele.classList.add('active-loading');
  },
  stop: function() {
    var ele = document.getElementById('wfLoading');
    if (ele) {
      ele.remove();
    }
  }
}


//function LoadingWithMask() {
//    //화면의 높이와 너비를 구합니다.
//    var maskHeight = $(document).height();
//    var maskWidth  = window.document.body.clientWidth;
//
//    //화면에 출력할 마스크를 설정해줍니다.
//    var mask       ="<div id='mask' style='position:absolute; z-index:9000; background-color:#000000; display:none; left:0; top:0;'></div>";
//    var loadingImg ='';
//
//    loadingImg +="<div id='loadingImg'>";
//    loadingImg +="<img src = \"/static/Spinner.gif\" 'style='position: absolute; display: block;margin:0 auto;'/>";
//    loadingImg +="</div>";
//
//    //화면에 레이어 추가
//    $('body')
//        .append(mask)
//        .append(loadingImg)
//
//    //마스크의 높이와 너비를 화면 것으로 만들어 전체 화면을 채웁니다.
//    $('#mask').css({
//            'width' : maskWidth
//            ,'height': maskHeight
//            ,'opacity' :'0.3'
//    });
//
//    //마스크 표시
//    $('#mask').show();
//
//    //로딩중 이미지 표시
//    $('#loadingImg').show();
//}
//function closeLoadingWithMask() {
//    $('#mask, #loadingImg').hide();
//    $('#mask, #loadingImg').remove();
//}



