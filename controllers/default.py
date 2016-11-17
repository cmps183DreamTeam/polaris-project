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

# NOMAD # ['_RAJ2000', '_DEJ2000', '_r', 'NOMAD1', 'USNO-B1', 'UCAC2', 'Tycho-2', 'f_Tycho-2', 'YM', 'RAJ2000', 'DEJ2000', 'r', 'e_RAJ2000', 'e_DEJ2000', 'pmRA', 'e_pmRA', 'pmDE', 'e_pmDE', 'Bmag', 'r_Bmag', 'Vmag', 'r_Vmag', 'Rmag', 'r_Rmag', 'Jmag', 'Hmag', 'Kmag', 'Xflags', 'R']
# UCAC # ['_RAJ2000', '_DEJ2000', '_r', 'UCAC4', 'RAJ2000', 'e_RAJ2000', 'DEJ2000', 'e_DEJ2000', 'ePos', 'EpRA', 'EpDE', 'f.mag', 'a.mag', 'e_a.mag', 'of', 'db', 'Na', 'Nu', 'Nc', 'pmRA', 'e_pmRA', 'pmDE', 'e_pmDE', 'MPOS1', 'UCAC2', 'Tycho-2', '_2Mkey', 'Jmag', 'e_Jmag', 'q_Jmag', 'Hmag', 'e_Hmag', 'q_Hmag', 'Kmag', 'e_Kmag', 'q_Kmag', 'Bmag', 'e_Bmag', 'f_Bmag', 'Vmag', 'e_Vmag', 'f_Vmag', 'gmag', 'e_gmag', 'f_gmag', 'rmag', 'e_rmag', 'f_rmag', 'imag', 'e_imag', 'f_imag', 'g', 'c', 'H', 'A', 'b', 'h', 'Z', 'B', 'L', 'N', 'S', 'LEDA', '_2MX']
# GSC # ['_RAJ2000', '_DEJ2000', '_r', 'GSC', 'RAJ2000', 'DEJ2000', 'PosErr', 'Pmag', 'e_Pmag', 'n_Pmag', 'Class', 'Plate', 'Epoch', 'Mult', 'Versions']
# USNO-B1 # ['_RAJ2000', '_DEJ2000', '_r', 'USNO-B1.0', 'Tycho-2', 'RAJ2000', 'DEJ2000', 'e_RAJ2000', 'e_DEJ2000', 'Epoch', 'pmRA', 'pmDE', 'muPr', 'e_pmRA', 'e_pmDE', 'fit_RA', 'fit_DE', 'Ndet', 'Flags', 'B1mag', 'B1C', 'B1S', 'B1f', 'B1s_g', 'B1xi', 'B1eta', 'R1mag', 'R1C', 'R1S', 'R1f', 'R1s_g', 'R1xi', 'R1eta', 'B2mag', 'B2C', 'B2S', 'B2f', 'B2s_g', 'B2xi', 'B2eta', 'R2mag', 'R2C', 'R2S', 'R2f', 'R2s_g', 'R2xi', 'R2eta', 'Imag', 'IC', 'IS', 'If', 'Is_g', 'Ixi', 'Ieta']
def mag_key(catalog):
    return {
        'NOMAD': 'Vmag',
        'UCAC': 'Vmag',
        'GSC': 'Pmag',
        'USNO-B1': 'R1mag',
    }[catalog]

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
    if len(result) > 0:
        for row in (result[0]):
            #create list with RA, DEC, mag values
            col_list = {}
            col_list['RA'] = float(row['_RAJ2000'])
            col_list['DEC'] = float(row['_DEJ2000'])
            col_list['mag'] = float(row[mag_key(cat)])
            #col_list = [float(result[0][x]['_RAJ2000']), float(result[0][x]['_DEJ2000']), float(result[0][x]['Vmag'])]
            dict[i] = col_list
            i = i + 1
    else:
        col_list = {}
        col_list['RA'] = float(0)
        col_list['DEC'] = float(0)
        col_list['mag'] = float(0)
        dict[0] = col_list
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
    in_dec = request.vars.dec
    in_rad = request.vars.rad
    #in_cat = request.vars.cat
    in_cat = "GSC" if (request.vars.cat) is None else (request.vars.cat)
    #call function to get coordinates
    cVega = celestial_target(in_ra, in_dec)
    #call find_guides
    call_dict = find_guides(cVega, in_cat, in_rad)
    return dict(dict = call_dict, reqs=request.vars)

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


