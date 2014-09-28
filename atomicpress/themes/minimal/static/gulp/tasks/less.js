"use strict";

var gulp = require("gulp"),
    less = require("gulp-less"),
    minifyCss = require("gulp-minify-css"),
    sourcemaps = require("gulp-sourcemaps"),
    cmq = require("gulp-combine-media-queries"),
    path = require("path"),
    rename = require("gulp-rename"),
    handleErrors = require("../util/handleErrors"),
    config = require("../config");

gulp.task("less", [ "lessDev", "lessProd", "lessIe" ]);

console.log(config.root);

gulp.task("lessDev", function() {
    gulp.src(path.join(config.root, "less", "main.less"))
        .pipe(sourcemaps.init())
        .pipe(less())
        .on("error", handleErrors.warning)
        .pipe(sourcemaps.write())
        .pipe(gulp.dest(path.join(config.root, "builds", "css")));
});

gulp.task("lessProd", function() {
    gulp.src(path.join(config.root, "less", "main.less"))
        .pipe(less())
        .on("error", handleErrors.warning)
        .pipe(cmq({
            log: true
        }))
        .pipe(minifyCss())
        .on("error", handleErrors.warning)
        .pipe(rename("main-min.css"))
        .pipe(gulp.dest(path.join(config.root, "builds", "css")));
});

gulp.task("lessIe", function() {
    gulp.src(path.join(config.root, "less", "ie.less"))
        .pipe(less())
        .on("error", handleErrors.warning)
        .pipe(gulp.dest(path.join(config.root, "builds", "css")));
});
