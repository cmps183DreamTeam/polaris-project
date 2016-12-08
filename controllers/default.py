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
    #
    db.results.truncate()
    redirect(URL('default', 'search'))
    return dict()

def mag_key(catalog):
    return {
        'NOMAD': 'Vmag',
        'UCAC': 'Vmag',
        'GSC': 'Pmag',
        'USNO-B1': 'R1mag',
    }[catalog]

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
    dict = []
    mag_type = 'None'
    if ((result is not None) and (len(result) > 0)):
        for row in (result[0]):
            #create list with RA, DEC, mag values
            col_list = {}
            col_list['RA'] = float(row['_RAJ2000'])
            col_list['DEC'] = float(row['_DEJ2000'])
            #col_list['mag'] = float(row[mag_key(cat)])#R1mag
            if (row['R1mag']) is not None:
                col_list['mag'] = float(row['R1mag'])
                mag_type = '1st'
            elif (row['R2mag']) is not None:
                col_list['mag'] = float(row['R2mag'])
                mag_type = '2nd'
            else:
                col_list['mag'] = 20.0
                #mag_type already intiated "None"
            if col_list['mag'] < 12.0:
                dict.append(col_list)
    else:
        col_list = {}
        col_list['RA'] = float(0)
        col_list['DEC'] = float(0)
        col_list['mag'] = float(0)
        #mag_type already intiated "None"
        dict.append(col_list)
    col_list['mag_type'] = mag_type   #initiated as "None", changes if an R1 or R2 value
    return dict

def search():
    import json
    none_ra = request.vars.ra is None
    none_dec = request.vars.dec is None
    none_rad = request.vars.rad is None
    if ( none_ra or none_dec or none_rad or none_wv):
        request.vars.ra = "0h0m0s"
        request.vars.dec = "+0s"
        request.vars.rad = "0s"
        request.vars.cat ='USNO-B1'
        request.vars.wavelength = 500.0
    in_ra = request.vars.ra
    in_dec = request.vars.dec
    in_rad = request.vars.rad
    in_wv = request.vars.wavelength
    #in_cat = 'USNO-B1' if (request.vars.cat) is None else (request.vars.cat)
    in_cat = 'USNO-B1'
    strehl = aprox_strehl_wv(in_wv)
    #call function to get coordinates
    cVega = celestial_target(in_ra, in_dec)
    #call find_guides
    call_dict = find_guides(cVega, in_cat, in_rad)
    json_str = json.dumps(call_dict)
    db.results.truncate()
    db.results.insert(datum=json_str)
    return dict(json_dict=json_str, reqs=request.vars, strehl=strehl)

def aprox_strehl_test():
    wvs = [0.05, 0.2, 0.35, 0.5, 0.65, 0.8, 0.95]
    result_array = []
    for wv in wvs:
        result_array.append(aprox_strehl_wv(wv))
    return response.json(result_array)

def aprox_strehl_wv(nanom):
    import math
    wavelength_reference = 0.5#'0.5 mu' #micrometer #500nm
    wv = nanom/1000.0
    wavelength = wv
    theta_const = 10.0#'10arcsec'    #10s
    theta_by_wavelength = theta_const*pow(wavelength/wavelength_reference, 5.0/6.0)
    sima_pow_2 = pow((theta_by_wavelength/theta_const), 5.0/3.0)
    strehl = pow(math.e, -1*sima_pow_2)
    return strehl

def aprox_strehl():
    import math
    wavelength_reference = 0.5#'0.5 mu' #micrometer #500nm
    wavelength = 0.65
    theta_const = 10.0#'10arcsec'    #10s
    theta_by_wavelength = theta_const*pow(wavelength/wavelength_reference, 5.0/6.0)
    sima_pow_2 = pow((theta_by_wavelength/theta_const), 5.0/3.0)
    strehl = pow(math.e, -1*sima_pow_2)
    #NGS
    return response.json(dict(strehl=strehl))
    # return strehl
    # return response.json(dict(
    #     wavelength_reference=wavelength_reference,
    #     wavelength=wavelength,
    #     theta_const=theta_const,
    #     wavelength_wavelength_reference=wavelength/wavelength_reference,
    #     pow__wavelength_wavelength_reference__5_6_=pow(wavelength_wavelength_reference, 5.0/6.0),
    #     theta_by_wavelength=theta_by_wavelength,
    #     sima_pow_2=sima_pow_2,
    #     strehl=strehl,
    #     pow_5_6 = pow(10, 5.0/6.0)
    # ))
# def aprox_strehl():
#     import math
#     wavelength_reference = '0.5 mu' #micrometer #500nm
#     theta_const = '10arcsec'    #10s
#     theta_const_by_wavelength = theta_const*(wavelength_reference)*pow((wavelength/wavelength_reference), 5/6)
#     sima_pow_2 = pow((theta_const_by_wavelength/theta_const), 5/3)
#     strehl = pow(math.e, -sima_pow_2)
#     #NGS
#     return strehl

def return_dict():
    saved_result = db().select(db.results.ALL).first()
    return response.json(saved_result["datum"])

def save_query():
    #in_ra = request.vars.ra
    #in_dec = request.vars.dec
    #in_rad = request.vars.rad
    #
    #form = SQLFORM(db.post).process()
    ## Add controls
    #form.add_button("Cancel", URL('default', 'index'))
    ## If all-correct perform edit, redirect home
    #if form.process().accepted:
    #    session.flash = 'new record inserted'
    #    redirect(URL('default', 'index'))
    #elif form.errors:
    #    session.flash = T("Can't process those values.")
    return

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


