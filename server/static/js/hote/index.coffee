filters = {}
initIndex = ($rootScope, $http) ->

    $http.get('/hote/list_project').success (data) ->
        $rootScope.projects = data.projects


ProjectListController = ($scope, $rootScope) ->

CreateProjectController = ($scope, $rootScope, $http) ->
    $scope.createProject = ->
        $http.post(
            '/hote/add_project',
            {
                url: $scope.projectUrl
                name: $scope.projectName
                desc: $scope.projectDesc
                year: $scope.startYear
                month: $scope.startMonth
                day: $scope.startDay
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