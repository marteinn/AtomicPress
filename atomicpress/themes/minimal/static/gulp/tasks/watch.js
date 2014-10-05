"use strict";

var gulp = require("gulp"),
    path = require("path"),
    config = require("../config");

gulp.task("watch", function() {
    gulp.watch(
        [ path.join("less", "**", "*.less") ],
        { cwd: config.root },
        [ "less" ]
    );
    gulp.watch(
        [ path.join("js", "**", "*.js") ],
        { cwd: config.root },
        [ "browserify" ]
    );
    gulp.watch(
        [ path.join("img", "**") ],
        { cwd: config.root },
        [ "images" ]
    );
});
