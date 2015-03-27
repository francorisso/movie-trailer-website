(function(){

	var app = angular.module('moviesController',[]);

	app.controller('MoviesCtrl',
		function( $scope, $http, $cookies, $location, $sce, $stateParams ){
			$scope.page   = 0;
			$scope.movie = {};
			$scope.movies = [];

			$(window).scroll(function(){
				clearTimeout( $scope.paginate_timer );
				$scope.paginate_timer = setTimeout(function(){
					$scope.paginate();
				},100);
			});

			$scope.get = function(){
				if($scope.loading){
					return;
				}

				$scope.loading = true;
				$scope.genre_name = $stateParams.genre_name;
				$http.get('/api/v1/movies',{
					'params' :
					{
						'page' 		: $scope.page,
						'genre'		: $scope.genre_name
					}
				})
				.success(function(data){
					var newMovies = [];
					for(var i=0; i<data.length; i++){
						$scope.movies.push( data[i] );
					}
					$scope.loading = false;
				})
				.error(function(data){
					$scope.loading = false;
				});

				$scope.page++;
			};
			$scope.get();

			$scope.paginate_timer = 0;
			$scope.paginate = function(){
				var position = parseInt( $(window).scrollTop() ) + parseInt( $(window).height() );
				var lastItemPosition = $('.movie-item:last').offset();
				lastItemPosition = lastItemPosition.top;
				if(position >= lastItemPosition){
					$scope.get();
				}
			};
		}
	);

	app.controller('MoviesDetailCtrl',
		function( $modalInstance, $scope, $http,
			$cookies, $location, $stateParams,
			$sce, $modal, $previousState
		){
			$scope.movie = {};
			$scope.trailer_url = '';

			$scope.closeModal = function(){
				$modalInstance.dismiss('close');
				$previousState.go('modalInvoker');
			};

			$scope.get = function(){
				$http.get('/api/v1/movies/' + $stateParams.id,{
					'params' :
					{
						'access_token' 	 : $scope.accessToken
					}
				})
				.success(function(data){
					$scope.movie = data;
					$scope.trailer_url = $sce.trustAsResourceUrl('https://www.youtube.com/embed/' + $scope.movie.trailer_youtube_url);
				})
				.error(function(data){
					console.error(data);
				});
			};
			$scope.get();
		}
	);

})();
