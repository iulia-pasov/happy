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
    app.controller('newMessageController', ['$http', function($http) {
        var vm = this;
        vm.message = {};
        vm.send = function() {
            console.log(vm.message);
            $http.post('http://happy.local/messages/', vm.message).then(function(data) {
             });
             vm.message = {};

        };
    }]);
    app.controller('ListController', function($http) {
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
