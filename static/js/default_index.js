// This is the js for the default/index.html view.

var app = function () {

    var self = {};

    Vue.config.silent = false; // don't show all warnings

    // enumerate/index posts on page
    var enumerate = function(v){
        var k=0;
        return v.map(function(f) {f._idx = k++;});
    };

    console.log('vue: default_index.js: app()');

    //enumerate();
    /*
    // Extends an array
    self.extend = function (a, b) {
        for (var i = 0; i < b.length; i++) {
            a.push(b[i]);
        }
    };



    // get posts url
    function get_posts_url(start_idx, end_idx) {
        var pp = {
            start_idx: start_idx,
            end_idx: end_idx
        };
        return posts_url + "?" + $.param(pp);
    }

    // get all posts
    self.get_posts = function () {
        $.getJSON(get_posts_url(0, 4), function (data) {
            self.vue.posts = data.posts;
            self.vue.has_more = data.has_more;
            self.vue.logged_in = data.logged_in;
            // index posts on page
            enumerate(self.vue.posts);
        })
    };

    // get more button
    self.get_more = function () {
        var num_posts = self.vue.posts.length;
        $.getJSON(get_posts_url(num_posts, num_posts + 4), function (data) {
            self.vue.has_more = data.has_more;
            self.extend(self.vue.posts, data.posts);
            // index posts on page
            enumerate(self.vue.posts);
        });
    };

    // add new button
    self.select_add_post = function () {
        // invert
        self.vue.is_adding_post = !self.vue.is_adding_post;
    };

    // add new post
    self.add_post = function () {
        if(self.vue.logged_in==false){
            alert("You must LoggedIn to POST");
            self.vue.form_artist="";
        }
        $.post(add_post_url,
            {
                title: self.vue.form_title,
                body: self.vue.form_body,
                first_name: self.vue.first_name,
                last_name: self.vue.last_name
            },
            function (data) {
                $.web2py.enableElement($("#add_post_submit"));
                self.vue.posts.unshift(data.post);
                self.vue.form_artist="";
                // index posts on page, hide forms
                enumerate(self.vue.posts);
                self.select_add_post();
            });
        self.vue.form_title="";
        self.vue.form_body="";
    };

    // delete icon
    self.delete_post = function (post_id) {
        $.post(del_post_url,
            {
                post_id: post_id
            },
            function () {
                var idx = null;
                for (var i = 0; i < self.vue.posts.length; i++) {
                    if (self.vue.posts[i].id === post_id) { idx = i + 1; break; }
                }
                if (idx) { self.vue.posts.splice(idx - 1, 1); }
                // index posts on page
                enumerate(self.vue.posts);
            }
        )
    };

    // edit icon
    self.select_edit_post = function (post_idx) {
        //hides all forms
        enumerate(self.vue.posts);
        self.vue.posts[post_idx].render_form = true;
        // assign old values
        self.vue.edit_form_title = self.vue.posts[post_idx].title;
        self.vue.edit_form_body = self.vue.posts[post_idx].body;
    };

    // submit button
    self.edit_post = function (post_idx) {
        if(self.vue.logged_in==false) {
            alert("You must be LoggedIn to Edit Posts");
            self.vue.form_artist="";
        }
        $.post(edit_post_url,
            {
                post_id: self.vue.posts[post_idx].id,
                title: self.vue.edit_form_title,
                body: self.vue.edit_form_body
            },
            function () {
                self.vue.posts[post_idx].title = self.vue.edit_form_title;
                self.vue.posts[post_idx].body = self.vue.edit_form_body;
                // I'm so sorry for the next line. I really HAD to add it...
                self.vue.posts[post_idx].updated_on = ((new Date()).getUTCFullYear() + '-' + ((new Date()).getUTCMonth()+1) + '-' + (new Date()).getUTCDate() + ' ' + (new Date()).getUTCHours() + ':' + (new Date()).getUTCMinutes() + ':' + (new Date()).getUTCSeconds());
                // hides forms
                enumerate(self.vue.posts);
            }
        )
    };

    // cancel button
    self.cancel_edit_post = function (post_idx) {
        self.vue.posts[post_idx].render_form = false;
        self.vue.posts[post_idx].title = self.vue.posts[post_idx].title + " ";
    }

    // structure
    self.vue = new Vue({
        el: "#vue-div",
        delimiters: ['${', '}'],
        unsafeDelimiters: ['!{', '}'],
        data: {
            is_adding_post: false,
            posts: [],
            logged_in: false,
            has_more: false,
            form_title: null,
            form_body: null,
            edit_form_title: null,
            edit_form_body: null
        },
        methods: {
            get_more: self.get_more,
            select_add_post: self.select_add_post,
            add_post: self.add_post,
            select_edit_post: self.select_edit_post,
            edit_post: self.edit_post,
            cancel_edit_post: self.cancel_edit_post,
            delete_post: self.delete_post
        }
    });

    self.get_posts();
    $("#vue-div").show();
    */
    /////////Bri's Code//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    self.vue = new Vue({
        el: "#vue-div",
        delimiters: ['${', '}'],
        unsafeDelimiters: ['!{', '}'],
        data: {
            products: [],
            cart: [],
            orders: [],
            product_search: '',
            cart_size: 0,
            cart_total: 0,
            page: 'prod'
        },
        methods: {
            get_products: self.get_products,
            inc_desired_quantity: self.inc_desired_quantity,
            inc_cart_quantity: self.inc_cart_quantity,
            buy_product: self.buy_product,
            goto: self.goto,
            do_search: self.get_products,
            pay: self.pay,
            wipe_cart: self.wipe_cart,
        }

    });

    return self;
};

// start
var APP = null;

// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function(){APP = app();});

// don't show debug
/*var APP = null;
// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function () {
    APP = app();
});*/
