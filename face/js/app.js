(function() {
    var app = angular.module('happy', [ ]);
    app.controller('HappiController', function () {
        this.test = 'iulia';
        });
    app.directive('messagePreview', function () {
        return {
            restrict: 'E',
            templateUrl: 'preview.html'
        };
    });
    app.controller('ListController', function($scope, $http) {
        var vm = this;
        $http.get('http://happy.local/messages/').then(function(data) {
            vm.messages = data.data.results;
        });
    });
    app.directive('listMessages', function() {
        return {
            restrict: 'E',
            templateUrl: 'list.html',
            controller: 'ListController',
            controllerAs: 'list'
        };
    });
})();
