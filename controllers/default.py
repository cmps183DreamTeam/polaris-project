# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    from astroquery.vizier import Vizier
    from astropy.coordinates import SkyCoord
    from astropy.coordinates import Angle
    # user_in_targ_ra = '18h36m56.33645s'
    # user_in_targ_dec = '+38d47m01.2802s'
    # cat=["NOMAD", "UCAC"]
    # rad = '5s'
    # # set target
    # cVega = celestial_target(user_in_targ_ra, user_in_targ_dec)
    # # call find_guides
    # call_dict = find_guides(cVega, cat, rad)
    #
    # response.flash = T("Hello World")
    # return dict(message=T('Welcome to web2py!'), call_dict=call_dict)
    #     form_type = 'create'
    #     form = SQLFORM(db.tel)
    #     #if form entered correctly, go to earch.html
    #     if form.process().accepted:
    #             redirect(URL('default', 'search'))
    #     return dict(form = form)
    return dict()

def test():
    redirect(URL('default', 'index'))
    response.flash = T(request.vars.name)
    return dict(name=request.vars.name)


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """

    return dict(form=auth())

def celestial_target(ra, dec):
    from astropy.coordinates import SkyCoord
    coords = SkyCoord(ra, dec)
    return coords

def find_guides(target, cat, rad):
    from astroquery.vizier import Vizier
    from astropy.coordinates import Angle
    result = Vizier.query_region(target, radius=rad, catalog=cat)
    dict = {}
    #run through each table in results
    # for x in range(0, len(result[0])-1):
    #     t with RA, DEC, mag values
    #     col_list = {}
    #     col_list['RA'] = float(result[0][x]['_RAJ2000'])
    #     col_list['DEC'] = float(result[0][x]['_DEJ2000'])
    #     col_list['mag'] = float(result[0][x]['Vmag'])
    #     #col_list = [float(result[0][x]['_RAJ2000']), float(result[0][x]['_DEJ2000']), float(result[0][x]['Vmag'])]
    #     dict[x] = col
    i = 0
    for row in (result[0]):
        #create list with RA, DEC, mag values
        col_list = {}
        col_list['RA'] = float(row['_RAJ2000'])
        col_list['DEC'] = float(row['_DEJ2000'])
        col_list['mag'] = float(row['Vmag'])
        #col_list = [float(result[0][x]['_RAJ2000']), float(result[0][x]['_DEJ2000']), float(result[0][x]['Vmag'])]
        dict[i] = col_list
        i = i + 1
    return dict

# def search():
#     user_in_targ_ra = '18h36m56.33645s'
#     user_in_targ_dec = '+38d47m01.2802s'
#     cat=["NOMAD", "UCAC"]
#     rad = '5s'
#     # set target
#     cVega = celestial_target(user_in_targ_ra, user_in_targ_dec)
#     # call find_guides
#     call_dict = find_guides(cVega, cat, rad)
#
#     if request.args(0) is not None:
#         boom = request.args(0)
#         return dict(boom = boom)
#
#     return dict(dict=call_dict)

# def search():
#     # get tel entered by user in db
#     t = db(db.tel.name == "Vega").select().first()
#     in_ra = t.ra
#     in_dec = t.decl
#     in_rad = t.rad
#     in_cat = t.cat
#     #user_in_targ_ra = '18h36m56.33645s'
#     #user_in_targ_dec = '+38d47m01.2802s'
#     #cat=["NOMAD", "UCAC"]
#     #rad = '5s'
#
#     #call function to get coordinates
#     cVega = celestial_target(in_ra, in_dec)
#     #call find_guides
#     call_dict = find_guides(cVega, in_cat, in_rad)
#     return dict(dict = call_dict)

def search():
    in_ra = request.vars.ra
    in_dec = request.vars.decl
    in_rad = request.vars.rad
    in_cat = request.vars.cat
    #call function to get coordinates
    cVega = celestial_target(in_ra, in_dec)
    #call find_guides
    call_dict = find_guides(cVega, in_cat, in_rad)
    return dict(dict = call_dict)

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


