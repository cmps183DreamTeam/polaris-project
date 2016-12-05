// This is the js for the default/index.html view.


var app = function () {
    console.log("WOW");
    var self = {};

    //Vue.config.silent = false; // don't show all warnings
    /////////Bri's Code//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    self.goto = function (page) {
        self.vue.page = page;
    };

    self.vue = new Vue({
        el: "#div1"

        data: {
            page: 'search'
        },
        methods: {
            goto: self.goto
        }

    });

    return self;
};

// start
var APP = null;

// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function(){APP = app();});
console.log("END");
// don't show debug
/*var APP = null;
// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function () {
    APP = app();
});*/
