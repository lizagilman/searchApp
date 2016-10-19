var app = angular.module('myApp', []).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('{$');
    $interpolateProvider.endSymbol('$}');
});

app.controller('myCtrl', function ($scope,$http) {
    $scope.searchStr = "";
    $scope.searchResult = [];
    $scope.urlToAdd = "";
    $scope.search = function () {
        $http.get("../search_query/?query="+$scope.searchStr).success(function (data) {
              console.log(data);
        });
    };

    $scope.addUrlToDb = function(){
          $http.get("../add_new_doc/?url="+$scope.urlToAdd).success(function (data) {
              console.log(data);
          });
    };

    $scope.searchResult.push({
          name:"Crawling",
          artist:"linkin park",
          text:"qqqqqqqqqqqqqqqqqqfewrg regerg"
      });
    $scope.searchResult.push({
            name: "Crawling 2",
            artist: "linkin park",
            text: "qqqqqqqqqqqqqqqqfdsfvbqqfewrg"
        }
    );
    console.log($scope.searchResult);
});