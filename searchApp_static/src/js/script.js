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
            $scope.searchResult = [];
           var searchResults = JSON.parse(data);
            console.log(searchResults);
            angular.forEach(searchResults, function (searchResult) {
                console.log(searchResult);
                $scope.searchResult.push(JSON.parse(searchResult));
            });
        });
    };

    $scope.addUrlToDb = function(){
          $http.get("../add_new_doc/?url="+$scope.urlToAdd).success(function (data) {
              console.log(data);
          });
    };

    console.log($scope.searchResult);
});