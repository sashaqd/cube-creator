import * as ns from './namespaces.js'

const allowed_regions = [
    "AG",
    "AI",
    "AR",
    "BE",
    "BL",
    "BS",
    "FR",
    "GE",
    "GL",
    "GR",
    "JU",
    "LU",
    "NE",
    "NW",
    "OW",
    "SG",
    "SH",
    "SO",
    "SZ",
    "TG",
    "TI",
    "UR",
    "VD",
    "VS",
    "ZG",
    "ZH",
    "CH"
]
function isAllowedRegion(quad) {

    let subject_has_region = (quad.subject.value.startsWith("https://health.ld.admin.ch/foph/covid19/vaccinated-population/")) || (quad.subject.value.startsWith("https://health.ld.admin.ch/foph/covid19/vaccine-doses/")) || (quad.subject.value.startsWith("https://health.ld.admin.ch/foph/covid19/affected/"))
    if (subject_has_region) {
        let n = quad.subject.value.lastIndexOf('/')
        let dimension = quad.subject.value.substring(n + 1);
        let region = dimension.substring(0, dimension.indexOf("-"))

        return allowed_regions.includes(region)
    }

    let object_has_region = (quad.object.value.startsWith("https://health.ld.admin.ch/foph/covid19/vaccinated-population/")) || (quad.object.value.startsWith("https://health.ld.admin.ch/foph/covid19/vaccine-doses/")) || (quad.object.value.startsWith("https://health.ld.admin.ch/foph/covid19/affected/"))
    if (object_has_region) {
        let n = quad.object.value.lastIndexOf('/')
        let dimension = quad.object.value.substring(n + 1);
        let region = dimension.substring(0, dimension.indexOf("-"))

        return allowed_regions.includes(region)
    }
    return true
}

export default isAllowedRegion
