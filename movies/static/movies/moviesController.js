(function(){

	var app = angular.module('moviesController',[]);

	app.controller('MoviesCtrl',
		function( $scope, $http, $cookies, $location, $sce, $stateParams ){
			$scope.page   = 0;
			$scope.movie = {};
			$scope.movies = [];
			$scope.genres = [];
			$scope.genreUrl = $stateParams.genre_url;

			$scope.genreChange = function(){
				$location.url('/genres/' + $scope.genreUrl);
			};

			$scope.reset = function(){
				$scope.movies = [];
				$scope.page = 0;
			};

			$scope.get = function(){
				if($scope.loading){
					return;
				}

				$scope.loading = true;
				$http.get('/api/v1/movies',{
					'params' :
					{
						'page' 		: $scope.page,
						'genre_url'	: $scope.genreUrl
					}
				})
				.success(function(data){
					$scope.movies = $scope.movies.concat(data);
					$scope.loading = false;
				})
				.error(function(data){
					$scope.loading = false;
				});

				$scope.page++;
			};

			//Set the genres
			$scope.genresGet = function(){
				$http.get('/api/v1/movies/genres',{})
				.success(function(data){
					$scope.genres = data;
				});
			};

			// Init functions
			$scope.genresGet();
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

			$(window).scroll(function(){
				clearTimeout( $scope.paginate_timer );
				$scope.paginate_timer = setTimeout(function(){
					$scope.paginate();
				},100);
			});
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

			$scope.$on("$stateChangeStart", function(evt, toState) {
	        	if (!toState.$$state().includes['modal']) {
	            	$modalInstance.dismiss('close');
	            }
	        });

			$scope.get();
		}
	);

})();
