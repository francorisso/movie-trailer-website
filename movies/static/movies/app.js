(function(){

	var app = angular.module('moviesTrailersApp',[
		'ngCookies',
		'moviesController', 
		'ui.bootstrap',
		'ui.router',
		'ct.ui.router.extras'
	]);

	app.config(['$stateProvider', '$urlRouterProvider', '$locationProvider', 
	function ($stateProvider, $urlRouterProvider, $locationProvider) { 
		$locationProvider.html5Mode(true);
		
		$urlRouterProvider.otherwise('/');

		$stateProvider
		.state('movies', {
			url: '/',
			name: 'top',
			views: {
				'app@': {
					templateUrl: '/static/movies/partials/list.html',
					controller: 'MoviesCtrl'
				},
			}
			
		})
		.state('modal', {
			url: '/movies/:id',
			name: 'modal',
			abstract: true,
  			sticky: true,
  			onEnter: ['$stateParams', '$state', '$modal', 
			function($stateParams, $state, $modal) {
        		$modal.open({
        			templateUrl: '/static/movies/partials/detail.html',
        			controller: 'MoviesDetailCtrl'
        		});
        	}]
		});
		
	}]);

})();
