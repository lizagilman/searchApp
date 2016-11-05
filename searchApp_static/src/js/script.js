var app = angular.module('myApp', []).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

app.controller('myCtrl', function ($scope,$http) {
    $scope.searchStr = "";
    $scope.searchResult = [];
    $scope.urlToAdd = "";
    $scope.loading = false;

    $scope.search = function (query) {
        $scope.loading=true;

        $http.get("../search_query/?query="+$scope.searchStr).success(function (data) {
            $('#resultsHeadline').html("Search results for: "+query);
            console.log(data);
            $scope.loading=false;
            $scope.searchResult = [];
            var searchResults = data;
            console.log(searchResults);
            angular.forEach(searchResults, function (searchResult) {
                //console.log(searchResult);
                searchResult.text = searchResult.text.substring(0,300);
                $scope.searchResult.push(searchResult);
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


    $scope.go = function(){
        var searchQuery = $('#searchInput').val();
        var songUrlToAdd = $('#addSongInput').val();
        if(searchQuery){
            $('#searchInput').val("")
            $scope.search(searchQuery);
        } else if(songUrlToAdd) {
            $('#addSongInput').val("")
            $scope.addUrlToDb(songUrlToAdd);
        } else {
            alert("Please insert input");
        }
    };

    console.log($scope.searchResult);
});