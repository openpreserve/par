/**
 * This package contains the Entity specific endpoints.
 * <p>
 * Each endpoint has a series of methods for retrieving a list of entities from a specific
 * Preservation Action Registry, as well as methods for creating, retrieving and updating individual entities.
 * <p>
 * Entity listing methods take "modified before/after" dates as parameters, as well as offset/limit integers.
 * Each of these parameters can safely be null to ignore their effects. For example, passing "null" to a
 * modifiedAfter date has the effect of returning all entities modified at any time up to the specified "modifiedBefore"
 * date. Similarly, using "null" for "modifiedBefore" will return all entities modified since the "modifiedAfter" date.
 * <p>
 * Passing "null" as the offset is equivalent to passing 0, passing "null" as the limit will return all entities beyond
 * the "offset".
 * <p>
 * Where there are "List" parameters, for example to filter Preservation Actions by the tool they use, these should not
 * be null, to ignore this filter an empty list should be passed.
 */

package org.parcore.api.client.endpoints;