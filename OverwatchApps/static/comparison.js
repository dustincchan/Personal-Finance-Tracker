var playerOne;
var playerTwo;

$(document).on('click', '#execute-player-search', function(){

  $.ajax({
    url: "https://api.lootbox.eu/pc/us/WorstHanzoNA-1566/profile",
    data: [],
    success: function(json){
      playerOne = json.data;
    },
    dataType: "json"
  });

  $.ajax({
    url: "https://api.lootbox.eu/pc/us/Mujang-11771/profile",
    data: [],
    success: function(json){
      playerTwo = json.data;
    },
    dataType: "json"
  });
});
