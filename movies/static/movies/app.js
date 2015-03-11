(function(){

	var app = angular.module("moviesTrailersApp",[
		"ngRoute", 
		"ngCookies",
		"moviesController", 
	]);

	app.config(['$routeProvider', '$locationProvider', 
	function ($routeProvider, $locationProvider) { 
		$locationProvider.html5Mode(true);
		
		$routeProvider
		.when("/", {
			templateUrl: "/static/movies/partials/list.html",
			controller: "MoviesCtrl"
		})
		.when("/movies/:id", {
			templateUrl: "/static/movies/partials/detail.html",
			controller: "MoviesDetailCtrl"
		});
		
	}]);

})();
