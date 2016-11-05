var app = angular.module('myApp', []).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

app.controller('myCtrl', function ($scope,$http) {
    $scope.searchStr = "";
    //$scope.searchResult = [];
    $scope.urlToAdd = "";
    $scope.loading = false;
    $scope.resultsHeadline = "";

    $scope.search = function (query) {
        $('#results').html("");
        $scope.resultsHeadline = "";
        //$('#resultsHeadline').html("");
        $scope.loading=true;
        $http.get("../search_query/?query="+$scope.searchStr).success(function (data) {
            $scope.loading=false;
            //$('#resultsHeadline').html("Search results for: "+query);
            $scope.resultsHeadline = "Search results for: " + query;
            //$scope.searchResult = [];
            var searchResults = data;
            //console.log(searchResults);
            angular.forEach(searchResults, function (searchResult) {
                var bolded_text = $scope.makeBold(searchResult.text, query.split(" "));
                searchResult.text = bolded_text.substring(0,300);
                //$scope.searchResult.push(searchResult);
                $('#results').append(" <div class='result'><h3><a ng-click='displaySong()'>" + searchResult.artist + " - " + searchResult.songName + "</a></h3><span>"+
                                        searchResult.text+" </span></div>");
            });
        });
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

    $scope.displaySong = function(){
        console.log("ng click");
        //$scope.resultsHeadline = "atrist - name";
        //$('#results').html("pure song text");
        // to do: put loading insted 67 & 68
        // $http.get("../getPlainSong/?query="+songId).success(function (data) {
        //         $('#results').html(data.plainText);
        // });
    };
});