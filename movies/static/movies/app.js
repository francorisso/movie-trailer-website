(function(){

	var app = angular.module('moviesTrailersApp',[
		'ngCookies',
		'moviesController',
		'ui.bootstrap',
		'ui.router',
		'ct.ui.router.extras',
		'ct.ui.router.extras.sticky'
	]);

	app.config(
	function ($stateProvider, $urlRouterProvider, $locationProvider, $stickyStateProvider) {
		$locationProvider.html5Mode(true);

		$urlRouterProvider.otherwise('/');

		$stateProvider
		.state('movies', {
			url: '/',
			name: 'top',
			sticky: true,
			views: {
				'app': {
					templateUrl: '/static/movies/partials/list.html',
					controller: 'MoviesCtrl'
				},
			}
		})
		.state('genres', {
			url: '/genres/:genre_url',
			name: 'genres',
			views: {
				'app': {
					templateUrl: '/static/movies/partials/list.html',
					controller: 'MoviesCtrl'
				},
			}
		})
		.state('modal', {
			url: '/movies/:id',
			name: 'modal',
			sticky: true,
			deepStateRedirect: true,
			template: '<div ui-view></div>',
			onEnter: showModal
		});
	});


	function showModal($modal, $previousState) {
      $previousState.memo("modalInvoker"); // remember the previous state with memoName "modalInvoker"
	  $modal.open({
        templateUrl:'/static/movies/partials/detail.html',
        backdrop: 'static',
        controller: 'MoviesDetailCtrl',
        windowClass: 'modal-detail'
      });
    }

})();
