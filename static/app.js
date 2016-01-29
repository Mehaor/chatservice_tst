/**
 * Created by Mihail on 29.01.16.
 */
TEMPLATE_PATH = '/static/templates/';

var chatApp = angular.module('chatApp', [
    'ngRoute',
    'chatControllers'
]);

chatApp.config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/threads', {
        templateUrl: TEMPLATE_PATH + 'threads.html',
        controller: 'ThreadListCtrl'
    }).when('/threads/:threadId', {
        templateUrl: TEMPLATE_PATH + 'thread.html',
        controller: 'ThreadDetailCtrl'

    }).otherwise({redirectTo: '/threads'});
}]);
