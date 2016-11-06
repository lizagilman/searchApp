var app = angular.module('myApp', []).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

app.controller('myCtrl', function ($scope,$compile,$http) {
    $scope.searchStr = "";
    $scope.searchResult = [];
    $scope.urlToAdd = "";
    $scope.loading = false;
    $scope.showResults = true;
    $scope.resultsHeadline = "";
    $scope.modalPlainText = "Loading...";
    $scope.allSongs=[];










    $scope.search = function (query) {
        $('#results').html("");
        $scope.resultsHeadline = "";
        //$('#resultsHeadline').html("");
        $scope.loading=true;


        $http.get("../search_query/?query="+$scope.searchStr).success(function (data) {
            $scope.loading=false;
            //$('#resultsHeadline').html("Search results for: "+query);
            $scope.resultsHeadline = "Search results for: " + query;
            $scope.searchResult = [];
            for (var key in data.res) {
                $scope.searchResult.push(data.res[key]);
            }
            angular.forEach($scope.searchResult, function (obj) {
                obj.plainText = obj.text;
                obj.text = obj.text.substring(0,300);
                obj.artist = obj.artist.toUpperCase();
            });
            //  console.log($scope.searchResult);
        });



        // $http.get("../search_query/?query="+$scope.searchStr).success(function (data) {
        //     $scope.loading=false;
        //     //$('#resultsHeadline').html("Search results for: "+query);
        //     $scope.resultsHeadline = "Search results for: " + query;
        //     $scope.searchResult = [];
        //     var searchResults = data;
        //     angular.forEach(searchResults, function (searchResult) {
        //         searchResult.plainText = searchResult.text;
        //         searchResult.text = searchResult.text.substring(0,300);
        //         searchResult.artist = searchResult.artist.toUpperCase();
        //         $scope.searchResult.push(searchResult);
        //
        //     });
        //});
    };






    $scope.addUrlToDb = function(url){
        $scope.loading = true;
        $http.get("../add_new_doc/?url="+url).success(function (data) {
            console.log(data);
            if(data=="success"){
                alert("Saved new song");
            } else {
                alert("Failed to save new song");
            }
            $scope.loading = false;
        });
    };



    $scope.getAllSongs = function(url){
        //$scope.loading = true;
        $scope.allSongs=[];
        $http.get("../apis/documents/").success(function (data) {
            var songs = data;
            angular.forEach(songs, function (song) {
                song.artist = song.artist.toUpperCase();
                $scope.allSongs.push(song)
            });

            //$scope.loading = false;
        });
    };


    $scope.deleteSong = function(id){
        //$scope.loading = true;
        console.log("clicked", id);
        $http.get("../deleteSong/"+id).success(function (data) {

        });
    };


    $scope.makeBold = function (input, wordsToBold){
        return input.replace(new RegExp('(\\b)(' + wordsToBold.join('|') + ')(\\b)','ig'), '$1<b>$2</b>$3');
    };

    $scope.go = function(){
        var searchQuery = $('#searchInput').val();
        var songUrlToAdd = $('#addSongInput').val();
        if(searchQuery){
            $('#searchInput').val("");
            $scope.search(searchQuery);
        } else if(songUrlToAdd) {
            $('#addSongInput').val("");
            $scope.addUrlToDb(songUrlToAdd);
        } else {
            alert("Please insert input");
        }
    };

    $scope.displaySong = function(id){
        console.log("ng click", id);
        $scope.searchResult.forEach( function (item, index) {
            if (item.id == id){
                $scope.modalPlainText = item.plainText;
            }
        });
        //$scope.resultsHeadline = "atrist - name";
        //$('#main').html("pure song text");
        // to do: put loading insted 67 & 68
        // $http.get("../getPlainSong/?query="+songId).success(function (data) {
        //         $('#results').html(data.plainText);
        // });
    };
});