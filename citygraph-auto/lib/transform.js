import rdf from 'rdf-ext'

const kantons = {
    "AG": 19,
    "AI": 16,
    "AR": 15,
    "BE": 2,
    "BL": 13,
    "BS": 12,
    "FR": 10,
    "GE": 25,
    "GL": 8,
    "GR": 18,
    "JU": 26,
    "LU": 3,
    "NE": 24,
    "NW": 7,
    "OW": 6,
    "SG": 17,
    "SH": 14,
    "SO": 11,
    "SZ": 5,
    "TG": 20,
    "TI": 21,
    "UR": 4,
    "VD": 22,
    "VS": 23,
    "ZG": 9,
    "ZH": 1,
}

function transformTriples(quad) {
    if (quad.predicate.value === "https://health.ld.admin.ch/foph/covid19/dimension/area") {
        let is_ch = quad.object.value === "CH"
        if (is_ch) {
            return rdf.quad(quad.subject, quad.predicate, rdf.namedNode("https://ld.admin.ch/country/CHE"))
        }
        let is_kanton = Object.keys(kantons).includes(quad.object.value);
        if (is_kanton) {
            return rdf.quad(quad.subject, quad.predicate, rdf.namedNode("https://ld.admin.ch/canton/" + kantons[quad.object.value]))
        }
    }
    return quad
}
export default transformTriples

