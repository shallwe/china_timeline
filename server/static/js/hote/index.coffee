filters = {}
initIndex = ($rootScope, $http) ->

    $http.get('/hote/project_list').success (data) ->
        $rootScope.project_list = data.project_list


ProjectListController = ($scope, $rootScope) ->

CreateProjectController = ($scope, $rootScope, $http) ->
    $scope.createProject = ->
        $http.post(
            '/add_project',
            {
                url: $scope.project_url
                name: $scope.project_name
                desc: $scope.project_desc
                year: $scope.start_year
                month: $scope.start_month
                day: $scope.start_day
            }
        ).success (data) ->
            initIndex()

angular.element(document).ready ->
    teamModule = angular.module 'index', []
    teamModule.config ($interpolateProvider) ->
        $interpolateProvider.startSymbol('[[')
        $interpolateProvider.endSymbol(']]')
    teamModule.filter filters
    teamModule.run initIndex
    teamModule.controller
        ProjectListController: ProjectListController
        CreateProjectController: CreateProjectController

    angular.bootstrap document, ['index']