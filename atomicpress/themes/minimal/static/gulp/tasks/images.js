"use strict";

var gulp = require("gulp"),
    changed = require("gulp-changed"),
	imagemin = require("gulp-imagemin"),
	path = require("path"),
	config = require("../config");

gulp.task("images", function() {
	gulp.src(path.join(config.root, "img", "**"))
		.pipe(changed(path.join(config.root, "builds", "img")))
		.pipe(imagemin())
		.pipe(gulp.dest(path.join(config.root, "builds", "img")));
});
