from pyramid.view import view_config
from pyramid.httpexceptions import (
    HTTPNotFound,
    HTTPBadRequest,
)
from sqlalchemy.exc import IntegrityError
from ..models import Matakuliah


def _validasi_integer_positif(nilai, nama_field: str):
    """Memastikan nilai bertipe integer dan bernilai lebih dari 0."""
    if isinstance(nilai, bool) or not isinstance(nilai, int) or nilai <= 0:
        raise ValueError(f'Field {nama_field} harus berupa bilangan bulat positif (> 0)!')
    return nilai


@view_config(route_name='matakuliah_list', renderer='json')
def matakuliah_list(request):
    """View untuk mengambil semua data matakuliah."""
    dbsession = request.dbsession
    daftar_mk = dbsession.query(Matakuliah).order_by(Matakuliah.id.asc()).all()
    return {'matakuliah': [mk.to_dict() for mk in daftar_mk]}


@view_config(route_name='matakuliah_detail', renderer='json')
def matakuliah_detail(request):
    """View untuk melihat detail satu matakuliah berdasarkan ID."""
    try:
        mk_id = int(request.matchdict['id'])
    except ValueError:
        return HTTPBadRequest(json_body={'error': 'ID matakuliah harus berupa angka!'})

    dbsession = request.dbsession
    mk = dbsession.query(Matakuliah).filter_by(id=mk_id).first()

    if mk is None:
        return HTTPNotFound(
            json_body={'error': f'Matakuliah dengan ID {mk_id} tidak ditemukan'}
        )

    return {'matakuliah': mk.to_dict()}


@view_config(route_name='matakuliah_add', request_method='POST', renderer='json')
def matakuliah_add(request):
    """View untuk menambahkan matakuliah baru dari payload JSON."""
    try:
        json_data = request.json_body
    except Exception:
        return HTTPBadRequest(json_body={'error': 'Payload request harus berupa JSON valid!'})

    required_fields = ['kode_mk', 'nama_mk', 'sks', 'semester']
    for field in required_fields:
        if field not in json_data or json_data[field] is None or str(json_data[field]).strip() == '':
            return HTTPBadRequest(json_body={'error': f'Field {field} wajib diisi!'})

    try:
        sks = _validasi_integer_positif(json_data['sks'], 'sks')
        semester = _validasi_integer_positif(json_data['semester'], 'semester')

        dbsession = request.dbsession
        mk_baru = Matakuliah(
            kode_mk=str(json_data['kode_mk']).strip(),
            nama_mk=str(json_data['nama_mk']).strip(),
            sks=sks,
            semester=semester,
        )
        dbsession.add(mk_baru)
        dbsession.flush()
        return {'success': True, 'matakuliah': mk_baru.to_dict()}

    except ValueError as err:
        return HTTPBadRequest(json_body={'error': str(err)})
    except IntegrityError:
        request.dbsession.rollback()
        return HTTPBadRequest(
            json_body={'error': f"Kode mata kuliah '{json_data['kode_mk']}' sudah terdaftar!"}
        )
    except Exception as err:
        return HTTPBadRequest(json_body={'error': str(err)})


@view_config(route_name='matakuliah_update', request_method='PUT', renderer='json')
def matakuliah_update(request):
    """View untuk memperbarui data matakuliah berdasarkan ID."""
    try:
        mk_id = int(request.matchdict['id'])
    except ValueError:
        return HTTPBadRequest(json_body={'error': 'ID matakuliah harus berupa angka!'})

    dbsession = request.dbsession
    mk = dbsession.query(Matakuliah).filter_by(id=mk_id).first()

    if mk is None:
        return HTTPNotFound(
            json_body={'error': f'Matakuliah dengan ID {mk_id} tidak ditemukan'}
        )

    try:
        json_data = request.json_body

        if 'kode_mk' in json_data:
            if not str(json_data['kode_mk']).strip():
                return HTTPBadRequest(json_body={'error': 'Field kode_mk tidak boleh kosong!'})
            mk.kode_mk = str(json_data['kode_mk']).strip()

        if 'nama_mk' in json_data:
            if not str(json_data['nama_mk']).strip():
                return HTTPBadRequest(json_body={'error': 'Field nama_mk tidak boleh kosong!'})
            mk.nama_mk = str(json_data['nama_mk']).strip()

        if 'sks' in json_data:
            mk.sks = _validasi_integer_positif(json_data['sks'], 'sks')

        if 'semester' in json_data:
            mk.semester = _validasi_integer_positif(json_data['semester'], 'semester')

        dbsession.flush()
        return {'success': True, 'matakuliah': mk.to_dict()}

    except ValueError as err:
        return HTTPBadRequest(json_body={'error': str(err)})
    except IntegrityError:
        dbsession.rollback()
        return HTTPBadRequest(json_body={'error': 'Kode mata kuliah sudah digunakan!'})
    except Exception as err:
        return HTTPBadRequest(json_body={'error': str(err)})


@view_config(route_name='matakuliah_delete', request_method='DELETE', renderer='json')
def matakuliah_delete(request):
    """View untuk menghapus matakuliah berdasarkan ID."""
    try:
        mk_id = int(request.matchdict['id'])
    except ValueError:
        return HTTPBadRequest(json_body={'error': 'ID matakuliah harus berupa angka!'})

    dbsession = request.dbsession
    mk = dbsession.query(Matakuliah).filter_by(id=mk_id).first()

    if mk is None:
        return HTTPNotFound(
            json_body={'error': f'Matakuliah dengan ID {mk_id} tidak ditemukan'}
        )

    dbsession.delete(mk)
    return {'success': True, 'message': f'Matakuliah dengan ID {mk_id} berhasil dihapus'}