const gulp = require('gulp');
const fs = require('fs');
const { spawn } = require('child_process')


let physics = spawn('python3', ['main.py'], {
  stdio: 'inherit'
})

gulp.task('watch', function() {

  gulp.watch('main.py', () => {
    console.log('file updated');

    physics.kill()

    physics = spawn('python3', ['main.py'], {
      stdio: 'inherit'
    })


  })
})

gulp.task('default', ['watch'])