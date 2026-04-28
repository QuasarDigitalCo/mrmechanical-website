/**
 * crmService.js — CRM integration stub for Mr Mechanical LP quiz leads
 *
 * PURPOSE:
 *   Receives a structured lead payload from the quiz form and forwards it
 *   to a CRM. Currently logs to console only. Wire in a real CRM by replacing
 *   the body of submitToCRM() with the appropriate SDK call or HTTP POST.
 *
 * HOW TO WIRE IN A CRM:
 *
 *   HubSpot (Forms API):
 *     POST https://api.hsforms.com/submissions/v3/integration/submit/{portalId}/{formGuid}
 *     Map: firstName→firstname, lastName→lastname, phone→phone, email→email,
 *          zipCode→zip, systemType/systemAge/mainProblem/urgency → custom properties
 *
 *   GoHighLevel (Contacts API):
 *     POST https://rest.gohighlevel.com/v1/contacts/
 *     Headers: Authorization: Bearer {API_KEY}
 *     Map: firstName, lastName, phone, email, postalCode (zipCode),
 *          customField: { systemType, systemAge, mainProblem, urgency }
 *
 *   Salesforce (REST API / Web-to-Lead):
 *     POST https://{instance}.salesforce.com/servlet/servlet.WebToLead
 *     Map: first_name, last_name, phone, email, zip, description (for quiz answers)
 *
 * PAYLOAD FIELDS:
 *   firstName    — contact first name
 *   lastName     — contact last name
 *   phone        — contact phone number
 *   email        — contact email address
 *   zipCode      — contact zip/postal code
 *   systemType   — Q1 answer value (e.g. "central_air_heat")
 *   systemAge    — Q2 answer value (e.g. "10_to_15")
 *   mainProblem  — Q3 answer value (e.g. "not_cooling_heating")
 *   urgency      — Q4 answer value (e.g. "emergency")
 *   submittedAt  — ISO 8601 timestamp of submission
 */

/**
 * @param {Object} payload
 * @param {string} payload.firstName
 * @param {string} payload.lastName
 * @param {string} payload.phone
 * @param {string} payload.email
 * @param {string} payload.zipCode
 * @param {string} payload.systemType
 * @param {string} payload.systemAge
 * @param {string} payload.mainProblem
 * @param {string} payload.urgency
 * @param {string} payload.submittedAt
 * @returns {Promise<void>}
 */
export async function submitToCRM(payload) {
  console.log('[CRM] Lead payload:', payload);
  return Promise.resolve();
}
