/**
 * Created with PyCharm.
 * User: kuznetsov-m
 * Date: 29.01.16
 * Time: 16:33
 * To change this template use File | Settings | File Templates.
 */

var chatControllers = angular.module('chatControllers', []);


chatControllers.controller('ThreadListCtrl', ['$scope', '$http', function($scope, $http) {
    $http.get('api/threads/').success(function(data) {$scope.threads = data});
    $scope.orderProp = '-last-message';
}]);

chatControllers.controller('ThreadDetailCtrl', ['$scope', '$http', '$routeParams', function($scope, $http, $routeParams) {

    $http.get('api/threads/' + $routeParams.threadId + '/').then(function(data) {
        $scope.thread = data.data;
        $scope.accessGranted = true;
        $scope.hello = 'hello';
    }, function() { $scope.accessGranted = false; });

}]);