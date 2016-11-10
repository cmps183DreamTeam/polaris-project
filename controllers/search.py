
def celestial_target(ra, dec):
    from astropy.coordinates import SkyCoord
    coords = SkyCoord(ra, dec)
    return coords

def find_guides(target, cat, rad):
    from astroquery.vizier import Vizier
    from astropy.coordinates import Angle
    result = Vizier.query_region(target, radius=rad, catalog=cat)
    dict = {}
    i = 0
    if len(result) > 0:
        for row in (result[0]):
            #create list with RA, DEC, mag values
            col_list = {}
            col_list['RA'] = float(row['_RAJ2000'])
            col_list['DEC'] = float(row['_DEJ2000'])
            #col_list['mag'] = float(row[mag_key(cat)])#R1mag
            if (row['R1mag']) is not None:
                col_list['mag'] = float(row['R1mag'])
            elif (row['R2mag']) is not None:
                col_list['mag'] = float(row['R2mag'])
            else:
                col_list['mag'] = '-'
            dict[i] = col_list
            i = i + 1
    else:
        col_list = {}
        col_list['RA'] = float(0)
        col_list['DEC'] = float(0)
        col_list['mag'] = float(0)
        dict[0] = col_list
    return dict

def search():
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
    return dict(dict = call_dict, reqs=request.vars)

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
