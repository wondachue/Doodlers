var SearchView = Backbone.View.extend({
	initialize: function(){
  		this.render();
	},
  	render: function() {
		var template = _.template($("#search_template").html(),{});
		this.$el.html(template);
	},
	events: {
		"click input[type=button]":"doSearch"
	},
	doSearch: function(event){
		alert("Search for " + $("#search_input").val());
	}
});

var search_view = new SearchView({el: $("#search_container")});
