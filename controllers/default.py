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
    #from astroquery.vizier import Vizier
    #from astropy.coordinates import SkyCoord
    #from astropy.coordinates import Angle
    #redirect(URL('default', 'search'))
    return dict()

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

def save_query():
    """
    import json
    cart_json = request.vars.cart
    cart_data = json.loads(cart_json)
    db.customer_order.insert(
        customer_info=request.vars.customer_info,
        #transaction_token=json.dumps(token),
        cart=request.vars.cart)
    for item in cart_data:
        for key in item:
            print("key: " + key + "->" + str(item[key]))
        row = db(db.product.id == item["id"]).select().first()
        row.quantity = row.quantity - item["cart_quantity"]
        row.update_record() # saves above change
    return response.json(cart_data)
    """
    import json
    return dict()


def celestial_target(ra, dec):
    from astropy.coordinates import SkyCoord
    coords = SkyCoord(ra, dec)
    return coords

def find_guides(target, cat, rad):
    from astroquery.vizier import Vizier
    from astropy.coordinates import Angle
    result = Vizier.query_region(target, radius=rad, catalog=cat)
    #dict = {}
    dict = []
    #i = 0
    mag_type = 'None'
    if len(result) > 0:
        for row in (result[0]):
            #create list with RA, DEC, mag values
            col_list = {}
            col_list['RA'] = float(row['_RAJ2000'])
            col_list['DEC'] = float(row['_DEJ2000'])
            #col_list['mag'] = float(row[mag_key(cat)])#R1mag
            #dict[1] will hold which magnitude we return
            if (row['R1mag']) is not None:
                col_list['mag'] = float(row['R1mag'])
                mag_type = '1st'
            elif (row['R2mag']) is not None:
                col_list['mag'] = float(row['R2mag'])
                mag_type = '2nd'
            else:
                col_list['mag'] = '-'
                #mag_type already intiated "None"
            #dict[i] = col_list
            dict.append(col_list)
            #i = i + 1
    else:
        col_list = {}
        col_list['RA'] = float(0)
        col_list['DEC'] = float(0)
        col_list['mag'] = float(0)
        #mag_type already intiated "None"
        #dict[0] = col_list
        dict.append(col_list)
    col_list['mag_type'] = mag_type   #initiated as "None", changes if an R1 or R2 value
    return dict

def search():
    if request.vars.ra is None:
        request.vars.ra = "0h0m0s"
        request.vars.dec = "+0s"
        request.vars.rad = "0s"
        request.vars.cat ='USNO-B1'

    in_ra = request.vars.ra
    in_dec = request.vars.dec
    in_rad = request.vars.rad
    #in_cat = request.vars.cat
    in_cat = 'USNO-B1' if (request.vars.cat) is None else (request.vars.cat)
    in_cat = 'USNO-B1'
    #call function to get coordinates
    cVega = celestial_target(in_ra, in_dec)
    #call find_guides
    call_dict = find_guides(cVega, in_cat, in_rad)

    import json
    json_str = json.dumps(call_dict)
    return dict(json_dict=json_str, dict = call_dict, reqs=request.vars)

def aprox_strehl():
    import math
    wavelength = 500.0 #nm
    wavelength_reference = 500.0 #micrometer #500nm
    theta_const = 10.0#'10arcsec'    #10s '10arcsec'
    theta_const_by_wavelength = theta_const*(wavelength_reference)*pow((wavelength/wavelength_reference), 5/6)
    print(theta_const_by_wavelength)
    sima_pow_2 = pow((theta_const_by_wavelength/theta_const), 5/3)
    strehl = pow(math.e, -sima_pow_2)
    #NGS
    #return strehl
    return response.json(dict(s=strehl))

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
    import json
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


