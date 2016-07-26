var playerOneProfileData;
var playerOneCharacterData = [];

var playerTwoProfileData;
var playerTwoCharacterData = [];

var offenseHeroes = "Genji,McCree,Pharah,Reaper,Soldier76,Tracer";
var defenseHeroes = "Bastion,Hanzo,Junkrat,Mei,Torbjoern,Widowmaker";
var tankHeroes = "D.Va,Reinhart,Roadhog,Winston,Zarya";
var supportHeroes = "Ana,Lucio,Mercy,Symmetra,Zenyatta";

var allHeroes = [offenseHeroes, defenseHeroes, tankHeroes, supportHeroes];

//level, games won/lost, playtime, avatar_img, rank, rank_img
function getProfileData(battleTag, platform, region) {
  $.ajax({
    url: "https://api.lootbox.eu/"+platform+"/"+region+"/"+battleTag+"/profile",
    data: [],
    success: function(json){
      return json.data;
    },
    dataType: "json"
  });
}

function getCharacterData(battleTag, platform, region, mode) {
  var allHeroesData = [];
  allHeroes.forEach(function(heroGroup){
    $.ajax({
      url: "https://api.lootbox.eu/"+platform+"/"+region+"/"+battleTag+"/"+mode+"/hero-multiple/"+heroGroup+"/",
      data: [],
      success: function(json){
        return json.data;
      }
    });
  });
}

$(document).on('click', '#execute-player-search', function(){

});
