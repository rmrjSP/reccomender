var express = require('express');
var router = express.Router();
var dbConn  = require('../db');

// display media page
router.get('/', function(req, res, next) {

    dbConn.query('SELECT * FROM media ORDER BY id desc',function(err,rows)     {

        if(err) {
            req.flash('error', err);
            // render to views/media/index.ejs
            res.render('media',{data:''});
        } else {
            // render to views/media/index.ejs
            res.render('media',{data:rows});
        }
    });
});

// display add media page
router.get('/add', function(req, res, next) {
    // render to add.ejs
    res.render('media/add', {
        name: '',
        author: '',
        type: '',
        description: '',
        tags: '',
        cover: '',
        rating: '',


    })
})
//deded//

// add a new media
router.post('/add', function(req, res, next) {

    let media_name = req.body.name;
    let media_author = req.body.author;
    let media_type = req.body.type;
    let media_description = req.body.description;
    let media_tags = req.body.tags;
    let media_cover = req.body.cover;
    let media_rating = req.body.rating 
    let errors = false;

    if(name.length === 0 || author.length === 0) {
        errors = true;

        // set flash message
        req.flash('error', "Please enter name and author");
        // render to add.ejs with flash message
        res.render('media/add', {
            media_name: media_name,
            media_author: media_author,
            media_type: media_type,
            media_description: media_description,
            media_tags: media_tags,
            media_cover: media_cover,
            media_rating: media_rating
        })
    }

    // if no error
    if(!errors) {

        var form_data = {
            media_name: media_name,
            media_author: media_author,
            media_type: media_type,
            media_description: media_description,
            media_tags: media_tags,
            media_cover: media_cover,
            media_rating: media_rating
        }

        // insert query
        dbConn.query('INSERT INTO media SET ?', form_data, function(err, result) {
            //if(err) throw err
            if (err) {
                req.flash('error', err)

                // render to add.ejs
                res.render('media/add', {
                    media_name: form_data.media_name,
                    media_author: form_data.media_author,
                    media_type: form_data.media_type,
                    media_description: form_data.media_description,
                    media_tags: form_data.media_tags,
                    media_cover: form_data.media_cover,
                    media_rating: form_data.media_rating
                })
            } else {
                req.flash('success', 'Media successfully added');
                res.redirect('/media');
            }
        })
    }
})

// display edit media page
router.get('/edit/(:id)', function(req, res, next) {

    let id = req.params.id;

    dbConn.query('SELECT * FROM media WHERE id = ' + id, function(err, rows, fields) {
        if(err) throw err

        // if user not found
        if (rows.length <= 0) {
            req.flash('error', 'No media not found with id = ' + id)
            res.redirect('/media')
        }
        // if media found
        else {
            // render to edit.ejs
            res.render('media/edit', {
                title: 'Edit Media',
                media_id: rows[0].media_id,
                media_name: rows[0].media_name,
                media_author: rows[0].media_author,
                media_type: rows[0].media_type,
                media_description: rows[0].media_description,
                media_tags: rows[0].media_tags,
                media_cover: rows[0].media_cover,
                media_rating: rows[0].media_rating
                
            })
        }
    })
})

// update media data
router.post('/update/:id', function(req, res, next) {

    let media_id = req.params.id;
    let media_name = req.body.name;
    let media_author = req.body.author;
    let media_type = req.body.type;
    let media_description = req.body.description;
    let media_tags = req.body.tags;
    let media_cover = req.body.cover;
    let media_rating = req.body.rating 
    let errors = false;

    if(name.length === 0 || author.length === 0) {
        errors = true;

        // set flash message
        req.flash('error', "Please enter name and author");
        // render to add.ejs with flash message
        res.render('media/edit', {
            media_id: req.params.id,
            media_name: media_name,
            media_author: media_author,
            media_type: media_type,
            media_description: media_description,
            media_tags: media_tags,
            media_cover: media_cover,
            media_rating: media_rating
        })
    }

    // if no error
    if( !errors ) {

        var form_data = {
            media_name: media_name,
            media_author: media_author,
            media_type: media_type,
            media_description: media_description,
            media_tags: media_tags,
            media_cover: media_cover,
            media_rating: media_rating
        }
        // update query
        dbConn.query('UPDATE media SET ? WHERE id = ' + media_id, form_data, function(err, result) {
            //if(err) throw err
            if (err) {
                // set flash message
                req.flash('error', err)
                // render to edit.ejs
                res.render('media/edit', {
                    id: req.params.id,
                    media_name: form_data.media_name,
                    media_author: form_data.media_author,
                    media_type: form_data.media_type,
                    media_description: form_data.media_description,
                    media_tags: form_data.media_tags,
                    media_cover: form_data.media_cover,
                    media_rating: form_data.media_rating
                })
            } else {
                req.flash('success', 'Media successfully updated');
                res.redirect('/media');
            }
        })
    }
})

// delete media
router.get('/delete/(:id)', function(req, res, next) {

    let media_id = req.params.id;

    dbConn.query('DELETE FROM media WHERE id = ' + media_id, function(err, result) {
        //if(err) throw err
        if (err) {
            // set flash message
            req.flash('error', err)
            // redirect to media page
            res.redirect('/media')
        } else {
            // set flash message
            req.flash('success', 'Media successfully deleted! ID = ' + id)
            // redirect to media page
            res.redirect('/media')
        }
    })
})

module.exports = router;