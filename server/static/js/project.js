// Generated by CoffeeScript 1.7.1
(function() {
  var run;

  run = function() {
    return createStoryJS({
      type: 'timeline',
      width: '100%',
      height: '600',
      lang: 'zh-cn',
      source: '/project_info?project_id=' + project_id,
      embed_id: 'timeline-div'
    });
  };

  $(function() {
    return run();
  });

}).call(this);